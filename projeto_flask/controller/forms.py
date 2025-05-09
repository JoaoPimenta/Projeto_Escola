from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, DateField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class criarProfessor(FlaskForm):
    nome = StringField("Nome: ", validators=[DataRequired()])
    idade = IntegerField("Idade: ", validators=[DataRequired()])
    materia = StringField("Matéria: ", validators=[DataRequired()])
    observacoes = TextAreaField("Observações: ", validators=[DataRequired()])
    confirmacao_create_prof = SubmitField("Criar")

class criarAluno(FlaskForm):
    nome = StringField("Nome: ", validators=[DataRequired()])
    idade = IntegerField("Idade: ", validators=[DataRequired(), NumberRange(min=1, max=100, message="Números de 0 a 100")])
    turma_id = IntegerField("ID da Turma: ", validators=[DataRequired()])
    data_nascimento = DateField("Data de Nascimento: ", validators=[DataRequired()])
    nota_semestre1 = FloatField("Nota do 1º Semestre: ", validators=[DataRequired()])
    nota_semestre2 = FloatField("Nota do 2º Semestre: ", validators=[DataRequired()])
    media = FloatField("Média Final", validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
    confirmacao_create_aluno = SubmitField("Criar")

class criarTurma(FlaskForm):
    nome = StringField("Nome da turma: ", validators=[DataRequired()])
    descricao = TextAreaField("Descrição: ", validators=[DataRequired()])
    professor_id = IntegerField("ID do Professor: ", validators=[DataRequired()])
    ativo = BooleanField("Essa turma está ativa? ", validators=[DataRequired()])
    confirmacao_create_turma = SubmitField("Criar")

class atualizarProfessor(FlaskForm):
    id = IntegerField("ID do(a) Professor(a): ", validators=[DataRequired()])
    nome = StringField("Nome: ", validators=[DataRequired()])
    idade = IntegerField("Idade: ", validators=[DataRequired()])
    materia = StringField("Matéria: ", validators=[DataRequired()])
    observacoes = TextAreaField("Observações: ", validators=[DataRequired()])
    confirmacao_update_prof = SubmitField("Atualizar")

class atualizarAluno(FlaskForm):
    id = IntegerField("ID do(a) Aluno(a): ", validators=[DataRequired()])
    nome = StringField("Nome: ", validators=[DataRequired()])
    idade = IntegerField("Idade: ", validators=[DataRequired(), NumberRange(min=1, max=100, message="Números de 0 a 100")])
    turma_id = IntegerField("ID da Turma: ", validators=[DataRequired()])
    data_nascimento = DateField("Data de Nascimento: ", validators=[DataRequired()])
    nota_semestre1 = FloatField("Nota do 1º Semestre: ", validators=[DataRequired()])
    nota_semestre2 = FloatField("Nota do 2º Semestre: ", validators=[DataRequired()])
    media = FloatField("Média Final", validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
    confirmacao_update_aluno = SubmitField("Atualizar")

class atualizarTurma(FlaskForm):
    id = IntegerField("ID da Turma: ", validators=[DataRequired()])
    nome = StringField("Nome da turma: ", validators=[DataRequired()])
    descricao = TextAreaField("Descrição: ", validators=[DataRequired()])
    professor_id = IntegerField("ID do Professor: ", validators=[DataRequired()])
    ativo = BooleanField("Essa turma está ativa? ", validators=[DataRequired()])
    confirmacao_update_turma = SubmitField("Atualizar")

class deletarProfessor(FlaskForm):
    id = IntegerField("ID do(a) Professor(a): ", validators=[DataRequired()])
    confirmacao_delete_prof = SubmitField("Deletar")

class deletarAluno(FlaskForm):
    id = IntegerField("ID do(a) Aluno(a): ", validators=[DataRequired()])
    confirmacao_delete_aluno = SubmitField("Deletar")

class deletarTurma(FlaskForm):
    id = IntegerField("ID da Turma: ", validators=[DataRequired()])
    confirmacao_delete_turma = SubmitField("Deletar")
    