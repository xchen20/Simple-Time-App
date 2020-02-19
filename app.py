from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time', methods = ['GET'])
def current_time():
    currentDT = datetime.datetime.now()
    return str(currentDT)

app.run(host='0.0.0.0',port=8080, debug=True)