from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board


boards_bp = Blueprint('boards', __name__, url_prefix='/boards')

def validate_board(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"Board {id} is invalid"}, 400))
        
    board = Board.query.get(id)
    
    if not board:
        abort(make_response({"message": f"Board {id} not found"}, 404))