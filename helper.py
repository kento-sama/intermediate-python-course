import logging

# logger = logging.getLogger(__name__)
# logger.info("Hello from helper")

logging.basicConfig(
    level=logging.DEBUG, # default logging level is warning and above
    format="{asctime} - {levelname} - {message}", # format how the logs will be displayed
    style="{", # will not run if there's no style in format
    filename=f"{__file__}.log", # creates a file named current_filename.log
    filemode="w" # w for rewriting the file and a for appending in the current existing file
)


def log_info(message, *args, **kwargs):
    logging.info(message, *args, **kwargs)
    

def log_debug(message, *args, **kwargs):
    logging.debug(message, *args, **kwargs)
    
    
def log_warning(message, *args, **kwargs):
    logging.warning(message, *args, **kwargs)
    
    
def log_error(message, *args, **kwargs):
    logging.error(message, *args, **kwargs)
    
    
def log_critical(message, *args, **kwargs):
    logging.critical(message, *args, **kwargs)


############################################    
""" logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler() # outputs on command line
file_h = logging.FileHandler("file.log") # outputs on file

# level and the format
stream_h.setLevel(logging.WARNING) # warnings and above will printed on the command line
file_h.setLevel(logging.ERROR) # error and above will be printed on a file

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error("This is an error") """
