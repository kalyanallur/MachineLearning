import sys

def create_error_message(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Exception occured in the file {filename}, line number {line_no}, details are {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details) :
        super().__init__(error_message)
        self.error_message = create_error_message(error_message,error_details=error_details)    

    def __str__(self):
        return self.error_message

#####################                  Testing exception file                       ###########################    

# if __name__=="__main__":   
#     try:
#         a = 1/0
#     except Exception as e:
#         raise CustomException(e,sys)