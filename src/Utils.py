import pickle
import os
import sys
from src.Exceptions import CustomException
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def save_model(object,path):
    try:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)

        with open(path,"wb") as file:
            pickle.dump(object, file)
    except Exception as e:
        raise CustomException(e,sys)
    
    
def evaluate_model(models, params,x_train,x_test,y_train,y_test):
    try: 
        #print(len(x_train),len(x_test),len(y_train),len(y_test))
        report = {}
        for i in range(len(list(models.keys()))):
            model = models[list(models.keys())[i]]
            param = params[list(models.keys())[i]]
            
            search = GridSearchCV(estimator = model, param_grid=param,cv=5)
            search.fit(x_train,y_train)
            
            model.set_params(**search.best_params_)
            model.fit(x_train,y_train)
            
            test_predict = model.predict(x_test)
            test_r2 = r2_score(y_test,test_predict)
            report[model] = test_r2
        return report
    

    except Exception as e:
        raise CustomException(e,sys)