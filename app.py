from flask import Flask, render_template

from extensions import db
from models import Grant

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

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
        archive=archive
    )

with app.app_context():
    db.create_all()

import scheduler

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)