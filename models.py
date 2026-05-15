from datetime import datetime
from extensions import db

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