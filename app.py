from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import scheduler

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

class Grant(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(500))

    url = db.Column(db.String(1000), unique=True)

    summary = db.Column(db.Text)

    relevance = db.Column(db.Integer)

    source = db.Column(db.String(300))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

@app.route("/")

def home():

    latest = Grant.query.order_by(
        Grant.created_at.desc()
    ).limit(25)

    archive = Grant.query.order_by(
        Grant.created_at.desc()
    ).offset(25)

    return render_template(
        "index.html",
        latest=latest,
        archive=archive
    )

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000)