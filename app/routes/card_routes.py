from app import db
from app.models.card import Card
from app.models.board import Board
from flask import Blueprint, jsonify, abort, make_response, request
import requests

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

def validate_card(card_id):
    try:
        id = int(card_id)
    except:
        abort(make_response({"message": f"Card {card_id} is invalid"}, 400))
        
    card = Card.query.get(card_id)
    
    if not card:
        abort(make_response({"message": f"Card {card_id} not found"}, 404))
        
    return card

@cards_bp.route("", methods=["POST"])
def create_card():
    if request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body or "description" not in request_body:
            return make_response(jsonify({"details": "Invalid data"}), 400)
        
    new_card = Card(
        title = request_body["title"],
        description = request_body["description"],
        like_count = request_body["like_count"],
        board_id = request_body["board_id"]
    )
    
    db.session.add(new_card)
    db.session.commit()
    card_dict = dict(card=new_card.to_dict())
    
    return make_response(jsonify(card_dict), 201)

@cards_bp.route("", methods=["GET"])
def get_cards():
    sort = request.args.get("sort")
    
    if sort == "asc":
        cards = Card.query.order_by(Card.title.asc()).all()
    else:
        cards = Card.query.order_by(Card.title.desc()).all()
        
    cards_list = []
    for card in cards:
        cards_list.append(card.to_dict())
    return jsonify(cards_list)

@cards_bp.route("/<card_id>", methods=["GET"])
def get_one_card(card_id):
    cards = validate_card(card_id)
    card_dict = dict(card=cards.to_dict())
    
    return make_response(jsonify(card_dict), 200)
