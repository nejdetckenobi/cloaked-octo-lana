from flask import Flask
from sample_project.routes.route import route
app = Flask(__name__)
app.register_blueprint(route)
