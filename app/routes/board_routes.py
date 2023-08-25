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
        if "title" not in request_body or "description" not in request_body:
            return make_response(jsonify({"details": "Invalid data"}), 400)
        
    new_board = Board(
        title = request_body["title"],
        description = request_body["description"]
    )
    
    db.session.add(new_board)
    db.session.commit()
    board_dict = dict(board=new_board.to_dict())
    
    return make_response(jsonify(board_dict), 201)

@boards_bp.route("", methods=["GET"])
def get_boards():
    sort = request.args.get("sort")
    
    if sort == "asc":
        boards = Board.query.order_by(Board.title.asc()).all()
    else:
        boards = Board.query.order_by(Board.title.desc()).all()
        
    boards_list = []
    for board in boards:
        boards_list.append(board.to_dict())
    return jsonify(boards_list)

# @boards_bp.route("/<id>", methods=["GET"])
# def get_one_board(id):
#     boards = validate_boards(id)
#     board_dict = dict(board=boards.to_dict())
    
#     return make_response(jsonify(board_dict), 200)