import os
import urllib.request as request
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.Common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig




class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        '''Fetch file from url and save to local directory
        '''

        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading dataset from :[{dataset_url}] into :[{zip_download_dir}]")
            
            # Extract Google Drive file ID
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export?format=download&id="
            gdown.download(
                url=prefix + file_id,
                output=str(zip_download_dir),
                quiet=False
            )

            logger.info(f"File downloaded successfully from {dataset_url} and saved to :[{zip_download_dir}] ") 

        except Exception as e:
            logger.exception(e)
            raise e


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file to the specified directory
        Function returns None
        """ 
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        logger.info("Extracting dataset zip file")
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Dataset zip file extracted successfully to :[{unzip_path}]")    


              