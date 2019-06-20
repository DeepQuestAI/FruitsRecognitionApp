from flask import (Flask, render_template, 
                url_for, redirect, request, abort)
from werkzeug.utils import secure_filename
import requests


app = Flask(__name__)

@app.route('/')
def index():
    form_string = "inline"
    prediction_string = "none"
    return render_template('form.htm', display_form = form_string, 
                                        display_results=prediction_string)

@app.route('/results')
def success():
    if(request.args.get('submission') != None):
        form_string = "none"
        prediction_string = "inline"
        return render_template('form.htm', display_form = form_string, 
                                        display_results=prediction_string,
                                        class_name=request.args.get('filepath'),
                                        confidence_score=request.args.get('filepath2'))
    else:
        return redirect(url_for('index'))

@app.route('/403')
def my_abort():
    return 'you have a long way to go'

@app.route('/submit', methods=['GET','POST'])
def form_submitted():
    if request.method == 'POST':

        try:
            sent_file = request.files['file']
            response = requests.post("http://localhost:80/v1/vision/custom/myCustomResNetModel",
                                                                files={"image":sent_file}).json()
            response_label = response["label"]
            response_confidence = response["confidence"]
            return redirect(url_for('success') + "?submission=True&filepath=" + str(response_label) 
                                            + "&filepath2=" + str(response_confidence))
        except:
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=4004)