from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello MSOE'
@app.route('/<name>')
def hello_name(name):
  return 'Hello '+ name