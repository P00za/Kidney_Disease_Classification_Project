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


  ### DVC cmd

  1. dvc init

  2. dvc repro
  
  3. dvc dag

  
  DVC
 
 - Its very lite weight for POC only
 
 - lite weight expriements tracker
 
 - It can perform Orchestration (Creating Pipelines)


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

 #with specific access

 1. EC2 access : It is virtual machine

 2. ECR: Elastic Container registry to save your docker image in aws

 #Description: About the deployment


 1. Build docker image of the source code

 2. Push your docker image to ECR

 3. Launch Your EC2

 4. Pull Your image from ECR in EC2

 5. Lauch your docker image in EC2


 #Policy:


 1. AmazonEC2ContainerRegistryFullAccess

 2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image


    - Save the URI: put your repo uri


## 4. Create EC2 machine (Ubuntu)


## 5. Open EC2 and Install docker in EC2 Machine:

 #optinal

 sudo apt-get update -y

 sudo apt-get upgrade

 #required

 curl -fsSL https://get.docker.com -o get-docker.sh

 sudo sh get-docker.sh

 sudo usermod -aG docker ubuntu

 newgrp docker


# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID= your aws access id

    AWS_SECRET_ACCESS_KEY= password

    AWS_REGION = ap-south-1

    AWS_ECR_LOGIN_URI= your uri

    ECR_REPOSITORY_NAME = repository name
