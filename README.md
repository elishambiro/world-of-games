# World of Games

[![CI/CD Pipeline](https://github.com/elishambiro/world-of-games/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/elishambiro/world-of-games/actions/workflows/ci-cd.yml)
[![Docker Image](https://img.shields.io/docker/pulls/elishambiro/project?logo=docker)](https://hub.docker.com/r/elishambiro/project)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com)
[![Prometheus](https://img.shields.io/badge/Prometheus-monitored-orange?logo=prometheus)](https://prometheus.io)
[![Grafana](https://img.shields.io/badge/Grafana-dashboard-yellow?logo=grafana)](https://grafana.com)

A Python-based gaming platform with three interactive games, a live leaderboard, and full observability via Prometheus + Grafana. Playable directly in the browser via a web terminal. Deployed via Docker and automated with GitHub Actions CI/CD.

---

## Games

| # | Game | Description |
|---|------|-------------|
| 1 | **Guess the Number** | Computer picks a random number — can you guess it? |
| 2 | **Memory Game** | Remember the sequence flashed on screen and type it back |
| 3 | **Currency Roulette** | Guess the ILS value of a random USD amount using live exchange rates |

All games support **difficulty levels 1–5**. Higher difficulty = more points.

---

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      Docker Compose                       │
│                                                          │
│  ┌──────────┐   ┌──────────┐   ┌────────────┐  ┌──────┐  │
│  │  Flask   │   │   ttyd   │   │ Prometheus │  │Grafana│ │
│  │  :5000   │   │  :7681   │   │   :9090    │  │:3001  │ │
│  └──────────┘   └──────────┘   └────────────┘  └──────┘  │
│       │               │               │                   │
│   Web UI +        Browser         Scrapes /metrics        │
│   /metrics        Terminal        every 15s               │
└──────────────────────────────────────────────────────────┘
```

- **Flask** — Web portal, leaderboard, `/metrics` endpoint
- **ttyd** — Web terminal embedded in browser to play games interactively
- **Prometheus** — Scrapes metrics every 15s
- **Grafana** — Pre-provisioned dashboard (HTTP rate, latency, game plays)

---

## Quick Start

### Prerequisites
- Docker & Docker Compose

### Run everything

```bash
git clone https://github.com/elishambiro/world-of-games.git
cd world-of-games
docker compose up -d
```

| Service | URL |
|---------|-----|
| Home / Leaderboard | http://localhost:5000 |
| Play Games (browser terminal) | http://localhost:5000/game |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3001 (admin/admin) |

---

## CI/CD — GitHub Actions

The pipeline runs automatically on every push to `master`:

```
Checkout → Build Docker image → Start container → Seed test data → E2E Tests (pytest) → Push to Docker Hub
```

### Secrets required

Add these in **GitHub → Settings → Secrets → Actions**:

| Secret | Description |
|--------|-------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |

---

## Monitoring

Prometheus scrapes `/metrics` from the Flask app every 15 seconds.

Grafana is pre-configured with a **World of Games** dashboard showing:
- HTTP request rate per endpoint
- Average request duration
- Total game plays by game type and result

Access Grafana at `http://localhost:3001` → login with `admin / admin`.

---

## Project Structure

```
world-of-games/
├── .github/workflows/ci-cd.yml   # GitHub Actions pipeline
├── games/
│   ├── GuessGame.py               # Guess the Number game
│   ├── MemoryGame.py              # Memory game
│   └── CurrencyRoulette.py        # Currency conversion game
├── monitoring/
│   ├── prometheus.yml             # Prometheus scrape config
│   └── grafana/provisioning/      # Auto-provisioned datasource + dashboard
├── templates/
│   ├── index.html                 # Home portal
│   ├── game.html                  # Browser terminal page
│   ├── score.html                 # Leaderboard UI
│   └── navbar.html                # Shared navigation bar
├── tests/
│   └── e2e.py                     # pytest end-to-end tests (API + Selenium)
├── app.py                         # Flask app (routes + Prometheus metrics)
├── score.py                       # SQLite score storage
├── menu.py                        # Game menu system
├── main.py                        # CLI entry point
├── Dockerfile                     # python:3.11-slim + ttyd binary
└── docker-compose.yml             # web + ttyd + prometheus + grafana
```

---

## Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/-Grafana-F46800?logo=grafana&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![Selenium](https://img.shields.io/badge/-Selenium-43B02A?logo=selenium&logoColor=white)
![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite&logoColor=white)

---

## Author

**Eli Shambiro** — DevOps Engineer

[![GitHub](https://img.shields.io/badge/GitHub-elishambiro-181717?logo=github)](https://github.com/elishambiro)
