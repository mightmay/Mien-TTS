from flask import Flask,render_template,request,send_file
from TTS.bin.mightTTS import mainsynthesize
myapp = Flask(__name__)

@myapp.route("/")
def myapp():
    
    return render_template('inputform.html')



 
@myapp.route('/outputform/', methods = ['GET','POST'])
def outputform():
   if request.method == 'GET':
        return f"ERROR called GET instead of POST"
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
 