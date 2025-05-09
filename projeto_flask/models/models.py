from projeto_flask import app
from projeto_flask import database

class Professor(database.Model):
    __tablename__ = "professor"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    idade = database.Column(database.Integer, nullable=False)
    materia = database.Column(database.String(100), nullable=False)
    observacoes = database.Column(database.Text, nullable=True)
    turmas = database.relationship('Turma', backref='professor', lazy=True)

class Turma(database.Model):
    __tablename__ = "turma"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    descricao = database.Column(database.Text, nullable=False)
    professor_id = database.Column(database.Integer, database.ForeignKey('professor.id'), nullable=False)
    ativo = database.Column(database.Boolean, nullable=True, default=True)
    alunos = database.relationship('Aluno', backref='turma', lazy=True)

class Aluno(database.Model):
    __tablename__ = "aluno"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    idade = database.Column(database.Integer, nullable=False)
    turma_id = database.Column(database.Integer, database.ForeignKey('turma.id'), nullable=False)
    data_nascimento = database.Column(database.Date, nullable=False)
    nota_semestre1 = database.Column(database.Float, nullable=False)
    nota_semestre2 = database.Column(database.Float, nullable=False)
    media = database.Column(database.Float, nullable=False)
    
with app.app_context():
    database.create_all()
    