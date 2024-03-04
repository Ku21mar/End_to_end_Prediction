import os ,sys
from pathlib import Path 
import logging


while True:
    project_name =input("Enter your project name:  ")
    if project_name != "":
        break


# f"{}/__init__.py",

list_of_files =[

        f"{project_name}/__init__.py",
        f"{project_name}/components/__init__.py",
        f"{project_name}/config/__init__.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/exception/__init__.py",
        f"{project_name}/constant/__init__.py",
        f"{project_name}/pipeline/__init__.py",
        f"{project_name}/utlis/__init__.py",
        f"{project_name}/entity/__init__.py",
        f"config/config.yaml",
        f"config/schema.yaml",
        "schema.yaml",
        "setup.py",
        "main.py",
        "app.py",
        "logs.py",
        "exception.py",
        "requirements.txt",
        "dvc.yaml"
                                                                
]



#Folder and Files spliting 

for filepath in list_of_files:
    filepath  =Path(filepath)
    filedir,filename  = os.path.split(filepath)



    if filedir != "":   # if the directory is not avialable them create the directory 
        os.makedirs(filedir,exist_ok =True)

    if (not os.path.exists(filepath)   or (os.apth.getsize(filepath)==0)):
        with open(filepath ,"w") as f:
            pass 

    else:
        logging.info(f"file is already present at {filepath}")



# if  __name__ ==__main__:
#     print(filedir)
#     print("\n")
#     print(filename)