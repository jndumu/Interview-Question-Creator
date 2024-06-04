import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py",

]

#Iterating over each file in the list
for filepath in list_of_files:
    # Converting filepath to a path object
    filepath = Path(filepath)
    # Spltting the filepath into directory and file
    filedir, filename = os.path.split(filepath)
    # Checking if the file's directory is not empty
    if filedir!="":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory {filedir} for the files {filename}")

    # Checking if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Creating an empty file if it doesn't exist or is empty
        with open(filepath , "w") as f:
            pass 
        # Logging the file creation of empty file
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists")
