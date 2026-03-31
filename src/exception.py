import sys 
from src.logger import logging
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # FIXED: Corrected exc_tb_lineno to exc_tb.tb_lineno and closed the parenthesis
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # FIXED: Moved the return statement outside of the .format() method
    return error_message

# FIXED: Added the missing colon at the end of the class definition
class CustomException(Exception):
    
    # FIXED: Added a space between def and __init__
    def __init__(self, error_message, error_detail: sys):
        # FIXED: Added parentheses to super()
        super().__init__(error_message)
        
        # FIXED: Corrected 'delf' to 'self', fixed variable naming, and corrected the keyword argument
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message