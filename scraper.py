from create_app import create_app

from extensions import db
from models import Grant

from scrapers.crawler import crawl
from scrapers.parser import extract_content
from scrapers.relevance import calculate_relevance
from scrapers.summarizer import summarize

from status import scraping_status

from datetime import datetime

SEED_URLS = [

    "https://vc4a.com",
    "https://solve.mit.edu",
    "https://www.gsma.com/mobilefordevelopment/",
    "https://linkedin.com"
]

app = create_app()

def run_scraper():

    scraping_status["running"] = True

    scraping_status["total_found"] = 0

    with app.app_context():

        # scraper logic here

        pass

    scraping_status["running"] = False

    scraping_status["last_run"] = str(datetime.utcnow())