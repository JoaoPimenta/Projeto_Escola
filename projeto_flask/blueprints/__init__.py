from flask import Blueprint

crud_bp = Blueprint('crud_bp', __name__)

from . import routes # importa as rotas para registrar no blueprint
