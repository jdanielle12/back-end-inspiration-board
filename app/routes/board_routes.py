from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board


boards_bp = Blueprint('boards', __name__, url_prefix='/boards')

def validate_boards(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"Board {id} is invalid"}, 400))
        
    board = Board.query.get(id)
    
    if not board:
        abort(make_response({"message": f"Board {id} not found"}, 404))
        
    return board

@boards_bp.route("", methods=["POST"])
def create_board():
    if request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body:
            return make_response(jsonify({"details": "Invalid data"}), 400)
    new_board = Board(
        title = request_body["title"]
    )
    
    db.session.add(new_board)
    db.session.commit()
    board_dict = dict(board=new_board.to_dict())
    
    return make_response(jsonify(board_dict), 201)
