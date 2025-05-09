from flask import render_template
from projeto_flask import database
from projeto_flask.models.models import Aluno
from blueprints import aluno_bp

@aluno_bp.route("/read/alunos", methods=["GET", "POST"])
def aluno():
    lista_alunos = database.session.query(Aluno).all()
    return render_template("alunos.html", lista_alunos=lista_alunos)
