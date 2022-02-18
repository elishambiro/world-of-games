import requests
from flask import Flask, request, render_template
from time import sleep

app = Flask("score")

@app.route('/')
def score():  
   return render_template("score.html")


@app.route('/get_scores')
def get_scores():  
    a_dictionary = []
    with open('templates/scores.txt', 'r') as a_file:
        for line in a_file:
            key, value = line.split()
            a_dictionary.append({"name": key, "score": value})
    return {"data": a_dictionary}
    

app.run(host='0.0.0.0', port=5000, debug=False)
