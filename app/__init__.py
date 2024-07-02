from flask import Flask

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'MINHA CHAVE SECRETONA'

from app.controller import routes
