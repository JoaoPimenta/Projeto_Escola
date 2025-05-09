from flask import render_template, redirect, url_for, flash, request
from projeto_flask import app
from projeto_flask import database
from projeto_flask.controller.forms import criarAluno, criarProfessor, criarTurma, atualizarAluno, atualizarProfessor, atualizarTurma, deletarProfessor, deletarAluno, deletarTurma
from projeto_flask.models.models import Professor, Aluno, Turma


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    criar_professor = criarProfessor()
    criar_aluno = criarAluno()
    criar_turma = criarTurma()

    if criar_professor.validate_on_submit() and "confirmacao_create_prof" in request.form:
        try:
            professor = Professor(nome=criar_professor.nome.data, idade=criar_professor.idade.data, materia=criar_professor.materia.data, observacoes=criar_professor.observacoes.data)
            database.session.add(professor)
            database.session.commit()
            flash(f"Criação do(a) Professor(a): {criar_professor.nome.data} bem sucedida!", "alert-success")
            return redirect(url_for("homepage"))
        
        except Exception as e:
            database.session.rollback()
            flash("Erro ao criar Professor: " + str(e), "alert-danger")

        if not criar_professor.validate_on_submit():
            flash("Erro ao validar formulário de professor: " + str(criar_professor.errors), "alert-danger")


    if criar_aluno.validate_on_submit() and "confirmacao_create_aluno" in request.form:

        try:
            aluno = Aluno(nome=criar_aluno.nome.data, idade=criar_aluno.idade.data, turma=Turma.query.get(criar_aluno.turma_id.data), data_nascimento=criar_aluno.data_nascimento.data, nota_semestre1 = criar_aluno.nota_semestre1.data, nota_semestre2 = criar_aluno.nota_semestre2.data, media=criar_aluno.media.data)
            database.session.add(aluno)
            database.session.commit()
            flash(f"Criação do(a) Aluno(a): {criar_aluno.nome.data} bem sucedida!", "alert-success")
            return redirect(url_for("homepage"))
        
        except Exception as e:
            database.session.rollback()
            flash("Erro ao criar Aluno: " + str(e), "alert-danger")

        if not criar_aluno.validate_on_submit():
            flash("Erro ao validar formulário de aluno: " + str(criar_aluno.errors), "alert-danger")        
    
    if criar_turma.validate_on_submit() and "confirmacao_create_turma" in request.form:
        try:
            turma = Turma(nome=criar_turma.nome.data, descricao=criar_turma.descricao.data, professor=Professor.query.get(criar_turma.professor_id.data), ativo=criar_turma.ativo.data)
            database.session.add(turma)
            database.session.commit()
            flash(f"Criação da Turma: {criar_turma.nome.data} bem sucedida!", "alert-success")
            return redirect(url_for("homepage"))
        
        except Exception as e:
            database.session.rollback()
            flash("Erro ao criar Turma: " + str(e), "alert-danger")
    
        if not criar_turma.validate_on_submit():
            flash("Erro ao validar formulário de turma: " + str(criar_turma.errors), "alert-danger")
    
    return render_template("create.html", criar_professor=criar_professor, criar_aluno=criar_aluno, criar_turma=criar_turma)


@app.route("/read", methods=["GET", "POST"])
def read():
    return render_template("read.html")


@app.route("/read/professor", methods=["GET", "POST"])
def professor():
    lista_professor = database.session.query(Professor).all()
    return render_template("professor.html", lista_professor=lista_professor)


@app.route("/read/alunos", methods=["GET", "POST"])
def aluno():
    lista_alunos = database.session.query(Aluno).all()
    return render_template("alunos.html", lista_alunos=lista_alunos)


@app.route("/read/turmas", methods=["GET", "POST"])
def turma():
    lista_turmas = database.session.query(Turma).all()
    return render_template("turmas.html", lista_turmas=lista_turmas)


@app.route("/update", methods=["GET", "POST"])
def update():
    atualizar_professor = atualizarProfessor()
    atualizar_aluno = atualizarAluno()
    atualizar_turma = atualizarTurma()


    if atualizar_professor.validate_on_submit() and "confirmacao_update_prof" in request.form:
        try:
            if Professor.query.get(atualizar_professor.id.data):
                database.session.query(Professor).filter(Professor.id == atualizar_professor.id.data).update({"nome": atualizar_professor.nome.data, "idade": atualizar_professor.idade.data, "materia": atualizar_professor.materia.data, "observacoes": atualizar_professor.observacoes.data})
                database.session.flush()
                database.session.commit()
                flash(f"Atualização do(a) Professor(a) ID:{atualizar_professor.id.data} bem sucedida!", "alert-warning")
                return redirect(url_for("homepage"))
            else:
                flash(f"O ID: {atualizar_professor.id.data} não é válido!", "alert-warning")
        except Exception as e:
            database.session.rollback()
            flash("Erro ao atualizar Professor: " + str(e), "alert-danger")

        if not atualizar_professor.validate_on_submit():
            flash("Erro ao validar formulário de professor: " + str(atualizar_professor.errors), "alert-danger")


    if atualizar_aluno.validate_on_submit() and "confirmacao_update_aluno" in request.form:
        try:
            if Aluno.query.get(atualizar_aluno.id.data):
                database.session.query(Aluno).filter(Aluno.id == atualizar_aluno.id.data).update({"nome": atualizar_aluno.nome.data, "idade": atualizar_aluno.idade.data, "turma": atualizar_aluno.turma_id.data, "data_nascimento": atualizar_aluno.data_nascimento.data, "nota_semestre1": atualizar_aluno.nota_semestre1.data, "nota_semestre2": atualizar_aluno.nota_semestre2.data, "media": atualizar_aluno.media.data})
                database.session.flush()
                database.session.commit()
                flash(f"Atualização do(a) aluno(a) ID:{atualizar_aluno.id.data} bem sucedida!", "alert-warning")
                return redirect(url_for("homepage"))
            else:
                flash(f"O ID: {atualizar_aluno.id.data} não é válido!", "alert-warning")
        except Exception as e:
            database.session.rollback()
            flash("Erro ao atualizar Aluno: " + str(e), "alert-danger")

        if not atualizar_aluno.validate_on_submit():
            flash("Erro ao validar formulário de aluno: " + str(atualizar_aluno.errors), "alert-danger")

    if atualizar_turma.validate_on_submit() and "confirmacao_update_turma" in request.form:
        try:
            if Turma.query.get(atualizar_turma.id.data):
                database.session.query(Turma).filter(Turma.id == atualizar_turma.id.data).update({"nome": atualizar_turma.nome.data, "descricao": atualizar_turma.descricao.data, "professor_id": atualizar_turma.professor_id.data, "ativo": atualizar_turma.ativo.data})
                database.session.flush()
                database.session.commit()
                flash(f"Atualização da Turma ID:{atualizar_turma.id.data} bem sucedida!", "alert-warning")
                return redirect(url_for("homepage"))
            else:
                flash(f"O ID: {atualizar_turma.id.data} não é válido!", "alert-warning")
        except Exception as e:
            database.session.rollback()
            flash("Erro ao atualizar Turma: " + str(e), "alert-danger")

        if not atualizar_turma.validate_on_submit():
            flash("Erro ao validar formulário de turma: " + str(atualizar_turma.errors), "alert-danger")

    return render_template("update.html", atualizar_professor=atualizar_professor, atualizar_aluno=atualizar_aluno, atualizar_turma=atualizar_turma)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    deletar_professor = deletarProfessor()
    deletar_aluno = deletarAluno()
    deletar_turma = deletarTurma()

    if deletar_professor.validate_on_submit() and "confirmacao_delete_prof" in request.form:
        try:
            if Professor.query.get(deletar_professor.id.data):
                database.session.query(Professor).filter(Professor.id == deletar_professor.id.data).delete()
                database.session.commit()
                flash(f"Professor ID: {deletar_professor.id.data} deletado com sucesso!", "alert-danger")
                return redirect(url_for("homepage"))
            else:
                flash(f"O ID: {deletar_professor.id.data} não é válido!", "alert-danger")
        except Exception as e:
            database.session.rollback()
            flash("Erro ao deletar Professor: " + str(e), "alert-danger")

        if not deletar_professor.validate_on_submit():
            flash("Erro ao validar formulário de professor: " + str(deletar_professor.errors), "alert-danger")
    
    if deletar_aluno.validate_on_submit() and "confirmacao_delete_aluno" in request.form:
        try:
            if Aluno.query.get(deletar_aluno.id.data):
                database.session.query(Aluno).filter(Aluno.id == deletar_aluno.id.data).delete()
                database.session.commit()
                flash(f"Aluno ID: {deletar_aluno.id.data} deletado com sucesso!", "alert-danger")
                return redirect(url_for("homepage"))
            else:
                flash(f"O ID: {deletar_aluno.id.data} não é válido!", "alert-danger")
        except Exception as e:
            database.session.rollback()
            flash("Erro ao deletar Aluno: " + str(e), "alert-danger")
    
        if not deletar_aluno.validate_on_submit():
            flash("Erro ao validar formulário de aluno: " + str(deletar_aluno.errors), "alert-danger")
    
    if deletar_turma.validate_on_submit() and "confirmacao_delete_turma" in request.form:
        try:
            if Turma.query.get(deletar_turma.id.data):
                database.session.query(Turma).filter(Turma.id == deletar_turma.id.data).delete()
                database.session.commit()
                flash(f"Turma ID: {deletar_turma.id.data} deletada com sucesso!", "alert-danger")
                return redirect(url_for("homepage"))
            else:
                flash(f"O ID: {deletar_turma.id.data} não é válido!", "alert-danger")
        except Exception as e:
            database.session.rollback()
            flash("Erro ao deletar Turma: " + str(e), "alert-danger")

        if not deletar_turma.validate_on_submit():
            flash("Erro ao validar formulário de turma: " + str(deletar_turma.errors), "alert-danger")        

    return render_template("delete.html", deletar_professor=deletar_professor, deletar_aluno=deletar_aluno, deletar_turma=deletar_turma)
