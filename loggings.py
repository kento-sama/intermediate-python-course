import helper

username = "Kent"

helper.log_debug("This is a debug message")
helper.log_info("This is an info message")
helper.log_warning("This is a warning message")
helper.log_error("This is an error message")
helper.log_critical("This is a critical message")

helper.log_critical(f"There was an error with the user: {username}")

a = 1
b = 0

try:
    c = a / b
except ZeroDivisionError as zde:
    #logging.critical(zde)
    helper.log_critical("Exception occured: ", exc_info=True)



