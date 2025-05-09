from flask import Flask
from .blueprints import crud_bp, professor_bp, aluno_bp, turma_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = '8751bba800902650b5feb5346c908fc3' # secrets.token_hex(16)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projeto.db"
app.config["HOST"] = '0.0.0.0'
app.config["PORT"] = 8000
app.config["DEBUG"] = True

database = SQLAlchemy(app) 

app.register_blueprint(crud_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(aluno_bp)
app.register_blueprint(turma_bp)

from projeto_flask.controller.routes import routes
