from app import app
from extensions import db
from models import Grant

from scrapers.crawler import crawl
from scrapers.parser import extract_content
from scrapers.relevance import calculate_relevance
from scrapers.summarizer import summarize

SEED_URLS = [

    "https://vc4a.com",
    "https://solve.mit.edu",
    "https://www.gsma.com/mobilefordevelopment/",
    "https://linkedin.com"
]

def run_scraper():

    print("Starting scraper...")

    with app.app_context():

        for site in SEED_URLS:

            links = crawl(site)

            for link in links[:20]:

                exists = Grant.query.filter_by(
                    url=link
                ).first()

                if exists:
                    continue

                content = extract_content(link)

                if not content:
                    continue

                relevance = calculate_relevance(content)

                if relevance >= 3:

                    summary = summarize(content)

                    grant = Grant(

                        title=link.split("/")[-1],

                        url=link,

                        summary=summary,

                        relevance=relevance,

                        source=site
                    )

                    db.session.add(grant)

                    print(f"Added: {link}")

        db.session.commit()

    print("Scraping completed.")