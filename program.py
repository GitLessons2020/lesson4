import random
import string

from flask import Flask
from idna import unicode

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base action'

@app.route('/v2')
def v2():
    return 'Second action'

@app.route('/de4d10ck')
def nguen_victor():
    length = 10
    return ''.join(random.choice(string.ascii_letters) for i in range(10))

