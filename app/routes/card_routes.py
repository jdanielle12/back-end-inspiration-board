from app import db
from app.models.card import Card
from flask import Blueprint, jsonify, abort, make_response, request
import requests

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")
