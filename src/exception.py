import sys
from src.logger import logging


def error_message_detail(error , error_detail:sys): # type: ignore
    """
    Build a detailed error message including file name, line number, and the original error message.
    Must be called inside an except block.
    """
    _,_,exc_tb=error_detail.exc_info()

    while exc_tb.tb_next: # type: ignore
        exc_tb = exc_tb.tb_next # type: ignore

    file_name = exc_tb.tb_frame.f_code.co_filename # type: ignore
    line_number = exc_tb.tb_lineno # type: ignore
    
    error_message = "Error occured in python script name [{0}] line number [{1}] err message[{2}]".format(
         file_name, line_number, str(error) # type: ignore
    )
    return error_message
   

class CustomException(Exception):
    def __init__(self, error_message , error_detail: sys): # type: ignore
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

        # Log automatically
        logging.error(self.error_message)


    def __str__(self):
        return self.error_message

# if __name__=="__main__":
    
 
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divided by zero")
#         raise CustomException(str(e), sys)
