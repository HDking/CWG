import os
from flask import Flask
from flask import Flask, render_template

from flask import request

app = Flask(__name__)

@app.route('/timeline')
def index():
    return render_template('/timeline.html')
    
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))