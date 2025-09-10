"""
exc_tb = It points to the place where the exception was caught(inside try block)

The first tb from sys.exc_info() is the outermost frame ( Where u cought the exception. )
tb_next = 1. Each traceback is like a linked list
          2. tb_next points to the next frame in the call stack(
          Closer to where the exception was originally raised. )
          3. By following .tb_next, you walk "deeper" into the stack.

"""
import sys
# Example( .tb_next )
def a():
    b()
def b():
    c()
def c():
    return 1 / 0 # <-- real error is here

try:
    a()
except Exception as e:
    print("Error has occured")   # <-- only tells error has occured not actual

    # In order to get acual error and its information we need
    # (  exc_type, exc_value, exc_tb = sys.exc_info()  )

    _,_,exc_tb = sys.exc_info()
    print("Traceback object: ", exc_tb)
    print("File name: ", exc_tb.tb_frame.f_code.co_filename) # type: ignore
    print("Line No: ", exc_tb.tb_lineno) # type: ignore
    print("Error Type: ", type(e).__name__)
    print("Error message: ",e)

    exc_type, exc_value, exc_tb = sys.exc_info()
    print("\nError Type: ", exc_type)
    print("Error Value: ", exc_value)
    print("Error traceback: ", exc_tb)






    # NOw if we use .tb_next will get exact line error
    # Walk to the deepest frame (where the real error occurred)
    tb_n = exc_tb
    while tb_n.tb_next: # type: ignore
        tb_n = tb_n.tb_next  # type: ignore
    
    # Extract file name and line number from the deepest frame
    file_name = tb_n.tb_frame. f_code. co_filename # type: ignore
    line_number =  tb_n.tb_lineno # type: ignore
    print(f"\nFile: {file_name}")
    print(f"Line Number: {line_number}")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")