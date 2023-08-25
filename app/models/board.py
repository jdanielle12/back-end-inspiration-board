from app import db

class Board(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String)
    description=db.Column(db.String)
    cards=db.relationship('Card', back_populates='Board')
