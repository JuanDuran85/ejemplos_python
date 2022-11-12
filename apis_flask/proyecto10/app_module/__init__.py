from flask import Flask
from app_module.principal.views_principal import index
from app_module.meet.views_meet import meet

app = Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(meet)