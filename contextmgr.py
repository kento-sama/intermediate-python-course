# with context manager
from contextlib import contextmanager

with open("notes.txt", mode="w") as file: # opens and closes the file automatically
    file.write("Hello world")
    
# without context manager
file = open("notes.txt", mode="w")

try:
    file.write("Goodbye, world")
finally:
    file.close()
    

class ManageFile:
    def __init__(self, filename):
        self.filename = filename
        
    def __enter__(self): # accessed using with keyword
        print("enter")
        self.file = open(self.filename, mode="w")
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("No exception")
        #print("exc:", exc_type, exc_value)
        print("exit")
        return True # not raise an exception
        
        
with ManageFile("notes.txt") as file: # __enter__
    print("do something")
    file.write("Hello again")
    file.somemethod()
# __exit__ after exiting the block

@contextmanager
def open_managed_file(filename):
    f = open(filename, mode="w")
    try:
        yield f # return f to be used while suspending its file closing
    finally:
        f.close()
        
with open_managed_file("notes.txt") as f:
    f.write("bye, again")