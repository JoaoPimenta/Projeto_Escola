from flask import render_template
from projeto_flask import database
from projeto_flask.models.models import Turma
from blueprints import turma_bp


@turma_bp.route("/read/turmas", methods=["GET", "POST"])
def turma():
    lista_turmas = database.session.query(Turma).all()
    return render_template("turmas.html", lista_turmas=lista_turmas)
