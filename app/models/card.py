from app import db


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    like_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey("board.board_id"), nullable=True)
    board = db.relationship("Board", back_populates="cards")
    
    def to_dict(self):
        card_dict = dict(
                card_id=self.card_id,
                title=self.title,
                description=self.description,
                like_count=self.like_count,
                board_id=self.board_id
            )
        if self.board_id:
            card_dict["board_id"] = self.board_id
            
        return card_dict
    