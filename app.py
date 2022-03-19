from flask import Flask,render_template,request,send_file
from TTS.bin.mightTTS import mainsynthesize
app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template('inputform.html')



 
@app.route('/outputform', methods = ['POST'])
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

if __name__ == '__main__':
	app.run()