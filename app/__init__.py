# esse é o arquivo __init__ do módulo principal "app".
# e é responsável pelas importações, instanciações e configurações do site

# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# instâncias e configurações
app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

# importações dos módulos responsáveis pelas rotas(default) e tabelas(tables)
from app.controllers import default
from app.models import tables