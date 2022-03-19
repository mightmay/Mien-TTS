from flask import Flask,render_template,request,send_file
from TTS.bin.mightTTS import mainsynthesize
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    
    return render_template('inputform.html')



 
@myapp.route('/outputform/', methods = ['POST', 'GET'])
def outputform():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to 'homepage' to submit form"
    if request.method == 'POST':
        input_form_data = request.form
        inputtext=request.form['inputtext']
        mainsynthesize(inputtext)
        try:
            return send_file('voice.wav', mimetype='audio/wav',as_attachment = True)
        except Exception as e:
            return str(e)
        
        outputmeesage = "Finished synthesizing: " + inputtext

        return outputmeesage
 