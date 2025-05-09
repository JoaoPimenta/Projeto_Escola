from flask import render_template
from projeto_flask import database
from projeto_flask.models.models import Professor
from blueprints import professor_bp

@professor_bp.route("/read/professor", methods=["GET", "POST"])
def professor():
    lista_professor = database.session.query(Professor).all()
    return render_template("professor.html", lista_professor=lista_professor)
