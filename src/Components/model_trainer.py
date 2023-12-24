import os
import sys
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.Exceptions import CustomException
from src.Utils import save_model, evaluate_model
from src.Logging import logging

class ModelTrainer:
    def __init__(self) :
        self.result_model_path = os.path.join(os.getcwd(),"artifacts","Model.pkl")
        self.models = {
            "LinearRegression":LinearRegression(),
            "RandomForestRegressor": RandomForestRegressor(),
            "AdaBoostRegressor":AdaBoostRegressor(),
            "GradientBoostingRegressor":GradientBoostingRegressor(),
            "DecisionTreeRegressor" : DecisionTreeRegressor(),
            "XGBRegressor":XGBRegressor()
        }

        self.params = {
            "LinearRegression" :{},
            "RandomForestRegressor":{
                                    "n_estimators" :[20,50,100,200,500],
                                    "criterion":['absolute_error', 'squared_error']},
            "AdaBoostRegressor" :{
                                 "n_estimators" :[20,50,100,200,500],
                                 "learning_rate":[0.01,0.1,1],
                                 "loss":["linear", "square","exponential"]},
            "GradientBoostingRegressor":{
                                        "loss" :["absolute_error","squared_error"],
                                        "n_estimators" :[20,50,100,200,500],
                                        "learning_rate":[0.01,0.1,1]},
            "DecisionTreeRegressor": {
                                    "splitter":["best","random"]},
            "XGBRegressor": {
                            "booster":["gbtree", "gblinear" ,"dart"],
                            "n_estimators" :[20,50,100,200,500],
                            "learning_rate":[0.01,0.1,1]

            }

        }

        
        
    def train_model(self,train_data,test_data):
        try:
            x_train = train_data[:,:-1]
            x_test = test_data[:,:-1]
            y_train = train_data[:,-1]
            y_test = test_data[:,-1]
            
            report = evaluate_model(self.models, self.params,x_train,x_test,y_train,y_test)
            logging.info("model training completed")
            models_list = sorted(report.items(), key=lambda x:x[1])
            best_model = models_list[0][0]
            r2score = models_list[0][1]
            print(report)
            print(best_model, r2score)

            save_model(best_model,self.result_model_path)
            logging.info("Model.pkl file generation completed")

        except Exception as e :
            raise CustomException(e,sys)