from flask import Flask
app = Flask(__name__)
from TTS.bin.mightTTS import mainsynthesize
@app.route("/")
def hello():
    mainsynthesize()
    return "Hello, World!"
