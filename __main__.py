import os
import sys
from shutil import copyfile
from py_compile import compile
dir_path = os.path.dirname(os.path.realpath(__file__))

tocompile = []

for file in os.getdir(dir_path):
    if file.endswith(".py"):
        tocompile.append(file)

for file in tocompile:
    try:
        compile(file)
    except:
        print("Error while compiling " + file)
        raise
    
print("Compiled files successfully!")
