from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from networksecurity.exception.exception import NetworkSecurityException
import logging
from networksecurity.logging import logger
from networksecurity.entity.config_entity import DataValidationConfig

import sys

if __name__=="__main__":
        try:
            trainingpipelineconfig=TrainingPipelineConfig()
            dataingestionconfig=DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
            data_ingestion=DataIngestion(data_ingestion_config=dataingestionconfig)
            logging.info("Initiating the data ingestion")
            dataingestionartifact=data_ingestion.initiate_data_ingestion()
            print(dataingestionartifact)
        except Exception as e:
            raise NetworkSecurityException(e,sys)