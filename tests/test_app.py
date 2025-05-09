import pytest
from projeto_flask import app

# Para rodar o teste -> python -m pytest tests/test_app.py -v

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bem-vindo" in response.data

def test_create_page(client):
    response = client.get('/create')
    assert response.status_code == 200
    assert b"Create" in response.data

def test_read_page(client):
    response = client.get('/read')
    assert response.status_code == 200
    assert b"Read" in response.data

def test_update_page(client):
    response = client.get('/update')
    assert response.status_code == 200
    assert b"Update" in response.data

def test_delete_page(client):
    response = client.get('/delete')
    assert response.status_code == 200
    assert b"Delete" in response.data

# def test_create_professor(client):
#     response = client.post('/create', data={
#         'nome': 'Prof. Teste',
#         'idade': 30,
#         'materia': 'Matemática',
#         'observacoes': 'Observações de teste',
#         'confirmacao_create_prof': 'Criar'
#     })
#     assert response.status_code == 302  # Redireciona após sucesso
#     assert b'Criação do(a) Professor(a): Prof. Teste bem sucedida!' in response.data

# def test_update_professor(client):
#     # Primeiro, criamos um professor
#     client.post('/create', data={
#         'nome': 'Prof. Teste',
#         'idade': 30,
#         'materia': 'Matemática',
#         'observacoes': 'Observações de teste',
#         'confirmacao_create_prof': 'Criar'
#     })

#     # Em seguida, tentamos atualizar
#     response = client.post('/update', data={
#         'id': 1,  # ID do professor que foi criado
#         'nome': 'Prof. Teste Atualizado',
#         'idade': 31,
#         'materia': 'Matemática Avançada',
#         'observacoes': 'Observações de teste atualizadas',
#         'confirmacao_update_prof': 'Atualizar'
#     })
#     assert response.status_code == 302
#     assert b'Atualização do(a) Professor(a) ID:1 bem sucedida!' in response.data

# def test_delete_professor(client):
#     # Primeiro, criamos um professor
#     client.post('/create', data={
#         'nome': 'Prof. Teste',
#         'idade': 30,
#         'materia': 'Matemática',
#         'observacoes': 'Observações de teste',
#         'confirmacao_create_prof': 'Criar'
#     })

#     # Em seguida, tentamos deletar
#     response = client.post('/delete', data={
#         'id': 1,  # ID do professor que foi criado
#         'confirmacao_delete_prof': 'Deletar'
#     })
#     assert response.status_code == 302
#     assert b'Professor ID: 1 deletado com sucesso!' in response.data

# def test_create_aluno(client):
#     # Primeiro, criamos um professor para associar ao aluno
#     client.post('/create', data={
#         'nome': 'Prof. Teste',
#         'idade': 30,
#         'materia': 'Matemática',
#         'observacoes': 'Observações de teste',
#         'confirmacao_create_prof': 'Criar'
#     })

#     # Agora, criamos um aluno
#     response = client.post('/create', data={
#         'nome': 'Aluno Teste',
#         'idade': 20,
#         'turma_id': 1,  # Assumindo que já existe uma turma
#         'data_nascimento': '2003-01-01',
#         'nota_semestre1': 7.5,
#         'nota_semestre2': 8.0,
#         'media': 7.75,
#         'confirmacao_create_aluno': 'Criar'
#     })
#     assert response.status_code == 302
#     assert b'Criação do(a) Aluno(a): Aluno Teste bem sucedida!' in response.data

# def test_update_aluno(client):
#     # Primeiro, criamos um aluno
#     client.post('/create', data={
#         'nome': 'Aluno Teste',
#         'idade': 20,
#         'turma_id': 1,  # Assumindo que já existe uma turma
#         'data_nascimento': '2003-01-01',
#         'nota_semestre1': 7.5,
#         'nota_semestre2': 8.0,
#         'media': 7.75,
#         'confirmacao_create_aluno': 'Criar'
#     })

#     # Em seguida, tentamos atualizar
#     response = client.post('/update', data={
#         'id': 1,  # ID do aluno que foi criado
#         'nome': 'Aluno Teste Atualizado',
#         'idade': 21,
#         'turma_id': 1,
#         'data_nascimento': '2003-01-01',
#         'nota_semestre1': 8.5,
#         'nota_semestre2': 9.0,
#         'media': 8.75,
#         'confirmacao_update_aluno': 'Atualizar'
#     })
#     assert response.status_code == 302
#     assert b'Atualização do(a) aluno(a) ID:1 bem sucedida!' in response.data

# def test_delete_aluno(client):
#     # Primeiro, criamos um aluno
#     client.post('/create', data={
#         'nome': 'Aluno Teste',
#         'idade': 20,
#         'turma_id': 1,
#         'data_nascimento': '2003-01-01',
#         'nota_semestre1': 7.5,
#         'nota_semestre2': 8.0,
#         'media': 7.75,
#         'confirmacao_create_aluno': 'Criar'
#     })

#     # Em seguida, tentamos deletar
#     response = client.post('/delete', data={
#         'id': 1,  # ID do aluno que foi criado
#         'confirmacao_delete_aluno': 'Deletar'
#     })
#     assert response.status_code == 302
#     assert b'Aluno ID: 1 deletado com sucesso!' in response.data

# def test_create_turma(client):
#     # Primeiro, criamos um professor
#     client.post('/create', data={
#         'nome': 'Prof. Teste',
#         'idade': 30,
#         'materia': 'Matemática',
#         'observacoes': 'Observações de teste',
#         'confirmacao_create_prof': 'Criar'
#     })

#     # Agora, criamos uma turma
#     response = client.post('/create', data={
#         'nome': 'Turma Teste',
#         'descricao': 'Descrição da turma teste',
#         'professor_id': 1,  # ID do professor que foi criado
#         'ativo': True,
#         'confirmacao_create_turma': 'Criar'
#     })
#     assert response.status_code == 302
#     assert b'Criação da Turma: Turma Teste bem sucedida!' in response.data

# def test_update_turma(client):
#     # Primeiro, criamos uma turma
#     client.post('/create', data={
#         'nome': 'Turma Teste',
#         'descricao': 'Descrição da turma teste',
#         'professor_id': 1,
#         'ativo': True,
#         'confirmacao_create_turma': 'Criar'
#     })

#     # Em seguida, tentamos atualizar
#     response = client.post('/update', data={
#         'id': 1,  # ID da turma que foi criada
#         'nome': 'Turma Teste Atualizada',
#         'descricao': 'Descrição atualizada da turma',
#         'professor_id': 1,
#         'ativo': False,
#         'confirmacao_update_turma': 'Atualizar'
#     })
#     assert response.status_code == 302
#     assert b'Atualização da Turma ID:1 bem sucedida!' in response.data

# def test_delete_turma(client):
#     # Primeiro, criamos uma turma
#     client.post('/create', data={
#         'nome': 'Turma Teste',
#         'descricao': 'Descrição da turma teste',
#         'professor_id': 1,
#         'ativo': True,
#         'confirmacao_create_turma': 'Criar'
#     })

#     # Em seguida, tentamos deletar
#     response = client.post('/delete', data={
#         'id': 1,  # ID da turma que foi criada
#         'confirmacao_delete_turma': 'Deletar'
#     })
#     assert response.status_code == 302
#     assert b'Turma ID: 1 deletada com sucesso!' in response.data