from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return('<h2> Welcome to TwitOff </h2>')
