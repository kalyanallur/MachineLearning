import os
import sys
from src.Logging import logging
from flask import Flask, render_template, request
from src.Pipelines.Predicting_pipeline import LoadFeatures, PredictPipe


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
        return render_template("home.html")

@app.route("/submit",methods = ["GET","POST"])
def sublit():
    if request.method=="GET":
            return render_template("home.html")
    else:
        obj = LoadFeatures(
        gender = request.form.get("gender"),
        race_ethnicity = request.form.get("ethnicity"),
        parental_level_of_education = request.form.get("parental_level_of_education"),
        lunch = request.form.get("lunch"),
        test_preparation_course = request.form.get("test_preparation_course"),
        reading_score = request.form.get("reading_score"),
        writing_score = request.form.get("writing_score"),
        )
        dataframe = obj.create_dataFrame()

        print(dataframe)
        pipe = PredictPipe()
        result = pipe.prediction(dataframe)
        return render_template("home.html",results = result)
    

if __name__=="__main__":
        app.run(host = "0.0.0.0", debug=True)