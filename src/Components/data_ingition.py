import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.Logging import logging
from src.Exceptions import CustomException


class DataIngestion:
    def __init__(self):
        # create_folder
        self.path = os.path.join(os.getcwd(),"artifacts")
        print(self.path)
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.datapath = os.path.join(self.path,"data.csv")
        self.train_path = os.path.join(self.path,"train_data.csv")
        self.test_path = os.path.join(self.path,"test_data.csv")

    def read_data(self,input_path):
        try:
            df = pd.read_csv(input_path)
            logging.info("Data Read completed")
            df.to_csv(self.datapath, header=True, index=False)
            logging.info("Data File generated")
            x_train,x_test = train_test_split(df, test_size=0.2, random_state=0)
            x_train.to_csv(self.train_path, header = True,index = False)
            x_test.to_csv(self.test_path, header = True,index = False)
            logging.info("Train and Test data generated")

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = DataIngestion()
    obj.read_data(r"C:\Users\HP\Downloads\stud.csv")