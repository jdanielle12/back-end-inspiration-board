from app import db

class Board(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String)
    description=db.Column(db.String)
    cards=db.relationship('Card', back_populates='Board')
    
    def to_dict(self, cards=False):
        board_dict={
            'id': self.id,
            'title': self.title,
            'description': self.description}
#Creates response body

