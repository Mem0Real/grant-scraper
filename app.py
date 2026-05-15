from flask import render_template

from create_app import create_app
from models import Grant
from extensions import db

from status import scraping_status

import threading

app = create_app()

@app.route("/")

def home():

    latest = Grant.query.order_by(
        Grant.created_at.desc()
    ).limit(25).all()

    archive = Grant.query.order_by(
        Grant.created_at.desc()
    ).offset(25).all()

    return render_template(
        "index.html",
        latest=latest,
        archive=archive,
        scraping=scraping_status
    )

@app.route("/scrape")

def scrape_now():

    from scraper import run_scraper

    if not scraping_status["running"]:

        thread = threading.Thread(
            target=run_scraper
        )

        thread.start()

    return {
        "status": "started"
    }

with app.app_context():

    db.create_all()

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)