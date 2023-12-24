import os
import sys
import pandas as pd
from src.Exceptions import CustomException
from src.Utils import load_model
from src.Logging import logging

class PredictPipe:
    def __init__(self) :
        self.preprocessor_path = os.path.join(os.getcwd(),"artifacts","preprocessor.pkl")
        self.model_path_path = os.path.join(os.getcwd(),"artifacts","Model.pkl")
        
    def prediction(self, data):
        try:
            preprocessor = load_model(self.preprocessor_path)
            model = load_model(self.model_path_path)
            preprocessed_data =  preprocessor.transform(data)
            predicted = model.predict(preprocessed_data)
            return predicted
        
        except Exception as e :
            raise CustomException(e,sys)
    
class LoadFeatures:
    def __init__(self,gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def create_dataFrame(self):
        try:
            input_dict = {"gender" : [self.gender],
            "race_ethnicity" : [self.race_ethnicity],
            "parental_level_of_education" : [self.parental_level_of_education],
            "lunch" : [self.lunch],
            "test_preparation_course" : [self.test_preparation_course],
            "reading_score" : [self.reading_score],
            "writing_score" : [self.writing_score]}

            return pd.DataFrame(input_dict)
        
        except Exception as e:
            raise CustomException(e,sys)