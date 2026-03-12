from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge
from score import get_all_scores, init_db

app = Flask("score")
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'World of Games Score Service', version='1.0.0')

game_plays = Counter(
    'game_plays_total',
    'Total game plays',
    ['game', 'difficulty', 'result']
)
scores_count_gauge = Gauge('scores_count', 'Total number of players in leaderboard')
top_score_gauge = Gauge('top_score', 'Highest score in leaderboard')
avg_score_gauge = Gauge('avg_score', 'Average score in leaderboard')

init_db()


def update_score_metrics():
    try:
        scores = [s['score'] for s in get_all_scores()]
        if scores:
            scores_count_gauge.set(len(scores))
            top_score_gauge.set(max(scores))
            avg_score_gauge.set(sum(scores) / len(scores))
    except Exception:
        pass


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/game')
def game():
    return render_template("game.html")


@app.route('/scores')
def score():
    return render_template("score.html")


@app.route('/get_scores')
def get_scores():
    data = get_all_scores()
    update_score_metrics()
    return {"data": data}


@app.route('/api/record_play', methods=['POST'])
def record_play_endpoint():
    data = request.get_json()
    game = data.get('game', 'unknown')
    difficulty = str(data.get('difficulty', '0'))
    result = data.get('result', 'unknown')
    game_plays.labels(game=game, difficulty=difficulty, result=result).inc()
    update_score_metrics()
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
