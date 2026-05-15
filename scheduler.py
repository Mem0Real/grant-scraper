from apscheduler.schedulers.background import BackgroundScheduler
from scraper import run_scraper

scheduler = BackgroundScheduler()

scheduler.add_job(
    func=run_scraper,
    trigger="interval",
    hours=6
)

scheduler.start()