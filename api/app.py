from flask import Flask, g
from flask_cors import CORS
from handlers.api import Api
from core.encode import encode
from core.core_conf import CoreConf
from core.core import Core
from app_session.app import AppSession


app = Flask("api")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app, version="v1", encode=encode)

app.config["MAX_PAGE_SIZE"] = 50
app.config["CORE_CONF"] = None
core_conf = CoreConf()
app_session = AppSession()


def init_app(config):
    app.config.update(config)
    app_session.init_app(app)
    return app


@app.before_request
def before_request():
    g.core = Core(app_session.get_session(), app.config["CORE_CONF"])
