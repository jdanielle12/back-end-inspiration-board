from app import db


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    like_count = db.Column(db.Integer, default=0)
    board = db.relationship("Board", back_populates="cards")
    board_id = db.Column(db.Integer, db.ForeignKey("board.id"))
    
    def to_dict(self):
        card_dict = dict(
                card_id=self.card_id,
                title=self.title,
                description=self.description,
                like_count=self.like_count,
                board_id=self.board_id
            )
        # if self.board_id:
        #     card_dict["board_id"] = self.board_id
            
        return card_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        new_obj = cls(
            title = data_dict["title"],
            description = data_dict["description"],
        )
        return new_obj