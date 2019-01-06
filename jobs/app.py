from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')