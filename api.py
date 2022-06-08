from flask import Flask
from src.routes.routes import app

app = Flask(__name__)

app.run(debug=True)