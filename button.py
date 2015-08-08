from flask import *

btn = Flask(__name__)

@app.route('/')
def home():
	