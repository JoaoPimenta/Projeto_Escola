from projeto_flask.db import database  # Importar o database diretamente
from sqlalchemy import Column, Integer, String, Text, Date, Float, Boolean

class Professor(database.Model):
    __tablename__ = "professor"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    materia = Column(String(100), nullable=False)
    observacoes = Column(Text, nullable=True)
    turmas = database.relationship('Turma', backref='professor', lazy=True)

class Turma(database.Model):
    __tablename__ = "turma"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    professor_id = Column(Integer, database.ForeignKey('professor.id'), nullable=False)
    ativo = Column(Boolean, nullable=True, default=True)
    alunos = database.relationship('Aluno', backref='turma', lazy=True)

class Aluno(database.Model):
    __tablename__ = "aluno"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    turma_id = Column(Integer, database.ForeignKey('turma.id'), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    nota_semestre1 = Column(Float, nullable=False)
    nota_semestre2 = Column(Float, nullable=False)
    media = Column(Float, nullable=False)
