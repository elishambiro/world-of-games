"""
End-to-end tests for World of Games.
Requires the Flask app running on localhost:5000.
Selenium tests require chromedriver installed on the host.
"""
import os
import shutil
import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "http://localhost:5000"
CHROMEDRIVER = shutil.which("chromedriver") or "/usr/local/bin/chromedriver"
HAS_CHROMEDRIVER = os.path.exists(CHROMEDRIVER)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def browser():
    if not HAS_CHROMEDRIVER:
        pytest.skip("chromedriver not found – skipping Selenium tests")
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER), options=opts)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def wait_for(driver, css, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css))
    )

# ---------------------------------------------------------------------------
# API tests (no browser needed)
# ---------------------------------------------------------------------------

def test_home_page():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"


def test_game_page():
    r = requests.get(f"{BASE_URL}/game")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"


def test_scores_page():
    r = requests.get(f"{BASE_URL}/scores")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"


def test_get_scores_schema():
    r = requests.get(f"{BASE_URL}/get_scores")
    assert r.status_code == 200
    body = r.json()
    assert "data" in body, "Response missing 'data' key"
    assert isinstance(body["data"], list), "'data' should be a list"


def test_get_scores_has_data():
    r = requests.get(f"{BASE_URL}/get_scores")
    data = r.json()["data"]
    assert len(data) > 0, "Leaderboard is empty – was test data seeded?"
    for entry in data:
        assert "name" in entry and "score" in entry
        assert isinstance(entry["score"], int) and entry["score"] > 0


def test_record_play_endpoint():
    r = requests.post(
        f"{BASE_URL}/api/record_play",
        json={"game": "guess", "difficulty": "3", "result": "win"},
    )
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


# ---------------------------------------------------------------------------
# Selenium UI tests
# ---------------------------------------------------------------------------

def test_leaderboard_table_visible(browser):
    browser.get(f"{BASE_URL}/scores")
    wait_for(browser, "#tbody tr")
    rows = browser.find_elements(By.CSS_SELECTOR, "#tbody tr")
    assert len(rows) > 0, "Leaderboard table has no rows"


def test_leaderboard_score_is_number(browser):
    browser.get(f"{BASE_URL}/scores")
    wait = WebDriverWait(browser, 10)
    # Wait until the score cell has non-empty text
    score_text = wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR, "#tbody tr:first-child td:nth-child(3)"
        ).text.strip() or None
    )
    assert score_text.isdigit(), f"Score cell is not a number: '{score_text}'"
    assert 1 <= int(score_text) <= 1_000_000


def test_leaderboard_search(browser):
    browser.get(f"{BASE_URL}/scores")
    wait_for(browser, "#tbody tr")
    total_rows = len(browser.find_elements(By.CSS_SELECTOR, "#tbody tr"))

    search = browser.find_element(By.ID, "search")
    search.send_keys("TestPlayer")
    time.sleep(0.4)

    filtered_rows = browser.find_elements(By.CSS_SELECTOR, "#tbody tr")
    assert len(filtered_rows) <= total_rows
    if filtered_rows:
        name = filtered_rows[0].find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
        assert "TestPlayer" in name


def test_navbar_links_present(browser):
    browser.get(f"{BASE_URL}/")
    for href in ["/", "/game", "/scores"]:
        link = browser.find_element(By.CSS_SELECTOR, f"a[href='{href}']")
        assert link.is_displayed(), f"Nav link {href} not visible"


def test_navbar_navigates_to_scores(browser):
    browser.get(f"{BASE_URL}/")
    browser.find_element(By.CSS_SELECTOR, "a[href='/scores']").click()
    WebDriverWait(browser, 5).until(EC.url_contains("/scores"))
    assert "/scores" in browser.current_url
