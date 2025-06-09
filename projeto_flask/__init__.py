from flask import Flask
from .db import database  # Importar o database aqui
import time
from sqlalchemy.exc import OperationalError
from .blueprints import crud_bp


def wait_for_db(app):
    with app.app_context():  # Cria um contexto de aplicação
        while True:
            try:
                # Tente criar uma conexão com o banco de dados
                with database.engine.connect() as conn:
                    break  # Se a conexão for bem-sucedida, saia do loop
            except OperationalError:
                print("Aguardando o MySQL estar disponível...")
                time.sleep(5)  # Aguarde 5 segundos antes de tentar novamente


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://projeto_user:projetopass@db/projeto'  # Corrigido
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    database.init_app(app)  # Inicializar o banco de dados com o app
    from .blueprints import crud_bp  # Importar apenas o crud_bp
    app.register_blueprint(crud_bp)

    wait_for_db(app)  # Aguarde o MySQL estar disponível

    with app.app_context():
        database.create_all()  # Criar as tabelas no contexto do app
    return app
