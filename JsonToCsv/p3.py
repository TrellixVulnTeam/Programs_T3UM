import datetime
from Logs import logpart
import sys
import time

def Multiplication(a, b):
    global mul1,mul2
    now3 = datetime.datetime.now()
    mul1=str(now3)

    print(a, "*", b, "=", a * b);this_line_number2 = sys._getframe().f_lineno;
    this_function_name2 = sys._getframe().f_code.co_name
    this_filename2 = sys._getframe().f_code.co_filename
    logpart(this_line_number2,this_function_name2,this_filename2,mul1)
