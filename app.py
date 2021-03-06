from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

import os
import inference

app = Flask(__name__) #creating app instance
Bootstrap(app) #passing the app into bootstrap

"""
@Routes
"""
@app.route('/', methods=['GET','POST']) #routing the app get request
def index() :
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name, n = inference.get_prediction(image_path)
            #print("Class Name : "+ class_name)
            result = {
                'class_name' : class_name,
                'image_path' : image_path,
                'n'          : n,
            }
            return render_template('show.html', result=result)
    return render_template('index.html') #to the html


if __name__ == '__main__' :
    app.run(debug = True)