from flask import (Flask, render_template, 
                url_for, redirect, request, abort)
from werkzeug.utils import secure_filename
import requests


app = Flask(__name__)


@app.route('/')
def index():
    """
    This method render the web app root or landing page 
    with the form contain the upload and submit button
    """
    form_string = "inline"
    prediction_string = "none"
    return render_template('form.htm', display_form = form_string, 
                                        display_results=prediction_string,
                                        preview_image="../static/img/strawberry.jpg")



@app.route('/results')
def success():
    """
    This method renders the page contain the rendered
    json results to the screen
    """
    if(request.args.get('submission') != None):
        form_string = "none"
        prediction_string = "inline"
        return render_template('form.htm', display_form = form_string, 
                                        display_results=prediction_string,
                                        class_name=request.args.get('label'),
                                        confidence_score=request.args.get('confidence'),
                                        preview_image="")
    else:
        return redirect(url_for('index'))



@app.route('/submit', methods=['GET','POST'])
def form_submitted():
    """
    This functions handle the form submission on the to DeepStack AI
    server
    """
    if request.method == 'POST':

        try:
            sent_file = request.files['file']
            sent_file_fullpath = request.form["filefullpath"]

            response = requests.post("http://localhost:80/v1/vision/custom/FruitsRecognition",
                                                                files={"image":sent_file}).json()
            response_label = response["label"]
            response_confidence = response["confidence"]
            return redirect(url_for('success') + "?submission=True&label=" + str(response_label)
                                            + "&confidence=" + str(response_confidence))
        except:
            return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True, port=81)