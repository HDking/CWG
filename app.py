import os
from flask import Flask

app = Flask(__name__)

@app.route('/crisis')
def index():
    return '<h1>Hello World</h1>'
    
@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, %s! </h1>' % name
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))