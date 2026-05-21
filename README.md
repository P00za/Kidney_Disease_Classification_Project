# Kidney_Disease_Classification_Project

....

### Workflows

1.  Update config.yaml
2.  Update secrets.yaml(Optional)
3.  Update params.yaml
4.  Update the entity
5.  Update the configuration manager in src config
6.  Update the components
7.  Update the pipeline
8.  Update the main.py
9.  Update the dvc.yaml
10. Update the app.py

....

# How to run?
....
### Steps:

Clone the repository

'''bash
https://github.com/P00za/Kidney_Disease_Classification_Project
'''
...
### Step 01- Create a conda environment after opening the repository

'''bash
conda create -n 'environment-name' python=3.8 -y
'''

'''bash 
conda activate 'environment-name'
'''


### Step 02 - install the requirements
'''bash 
pip install -r requirements.txt
'''





### MLFLOW

[Documentation](https://mlflow,org/docs/latest/index.html)

#### cmd
- mlflow ui

### dagshub

[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI="https://dagshub.com/P00za/Kidney_Disease_Classification_Project.mlflow"

MLFLOW_TRACKING_USERNAME="P00za"

MLFLOW_TRACKING_PASSWORD="Your Token"


  Run this to export as env variables:

  '''bash

 export  MLFLOW_TRACKING_URI="https://dagshub.com/P00za/Kidney_Disease_Classification_Project.mlflow"

 export MLFLOW_TRACKING_USERNAME="P00za"

 export MLFLOW_TRACKING_PASSWORD="Your Token"

  '''