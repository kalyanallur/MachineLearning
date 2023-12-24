import os
import sys
from src.Exceptions import CustomException
from src.Logging import logging
import pandas as pd
import numpy as np 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.Utils import save_model
class Datatransformation:
    def __init__(self):
        self.preprocessor_path = os.path.join(os.getcwd(),"artifacts","preprocessor.pkl")
    def data_Preprocessing(self):
        try:
            num_columns = ['reading_score', 
                        'writing_score']
            cat_columns = ['gender', 
                        'race_ethnicity', 
                        'parental_level_of_education', 
                        'lunch', 
                        'test_preparation_course']

            num_pipeline= Pipeline(
                [
                    ("imputing", SimpleImputer(strategy="median")),
                    ("scaling",StandardScaler())
                ]
            )

            cat_pipelie = Pipeline(steps=[
                ("imputing", SimpleImputer(strategy="most_frequent")),
                ("encoding", OneHotEncoder()),
                ("scaling",StandardScaler(with_mean=False))

            ])

            preprocessor= ColumnTransformer([("num_transformation", num_pipeline, num_columns),
                                            ("cat_transformation", cat_pipelie, cat_columns)])

            return preprocessor
        
        except Exception as e:
             raise CustomException(e,sys)
    
    def initiate_data_preprocessing(self, train_data_path, test_data_path):
            try:
                train_df =pd.read_csv(train_data_path)
                test_df = pd.read_csv(test_data_path)

                logging.info("Train and test data loaded")

                x_training_data = train_df.drop("math_score",axis=1) 
                y_train = train_df["math_score"]
                x_testing_data = test_df.drop("math_score",axis=1) 
                y_test = test_df["math_score"]
                preprocessing_obj = self.data_Preprocessing()
                x_train = preprocessing_obj.fit_transform(x_training_data)
                x_test = preprocessing_obj.transform(x_testing_data)
                preprocessed_train_data= np.concatenate([x_train,np.array(y_train).reshape(-1,1)], axis=1)
                preprocessed_test_data = np.concatenate([x_test,np.array(y_test).reshape(-1,1)], axis=1)
                logging.info("data preprocessing is completed")
                
                save_model(preprocessing_obj,self.preprocessor_path)
                logging.info("preprocessor.pkl Generated")
                return preprocessed_train_data, preprocessed_test_data

            except Exception as e:
                 raise CustomException(e,sys)