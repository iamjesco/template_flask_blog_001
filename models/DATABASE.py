from app import db
from datetime import datetime as dt


class Post(db.Model):
	pk = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False, unique=True)
	body = db.Column(db.Text(3000), nullable=False)
	author = db.Column(db.String(100), default='Jesco')
	created = db.Column(db.DateTime, default=dt.utcnow)
	
	def __repr__(self):
		return f'{self.title}'


db.create_all()