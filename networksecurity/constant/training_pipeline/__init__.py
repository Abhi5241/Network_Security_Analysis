import os
import sys
import numpy as np
import pandas as pd

TARGET_COLUMN="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="NetworkData.csv"

TRAIN_FILE_NAME:str="Train.csv"
TEST_FILE_NAME:str="Test.csv"

PREPROCESSING_OBJECT_FILE_NAME="preprocessing.pkl"
MODEL_FILE_NAME:str="model.pkl"
SCHEMA_DROP_COLS="drop_columns"
SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")
SAVED_MODEL_DIR=os.path.join("saved_models")


DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="KNAcademy"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2

DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"

DATA_TRANSFORMATION_DIR_NAME:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str="transformed_object"


DATA_TRANSFORMATION_IMPUTER_PARAMS:dict={
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights": "uniform",
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH:str="train.npy"
DATA_TRANSFORMATION_TEST_FILE_PATH:str="test.npy"

MODEL_TRAINER_DIR_NAME:str="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str="model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float=0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD:float=0.5

MODEL_EVALUATION_DIR_NAME:str="model_evaluation"
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE:float=0.02
MODEL_EVALUATION_REPORT_NAME="report.yaml"

MODEL_PUSHER_DIR_NAME="model_pusher"
MODEL_PUSHER_SAVED_MODEL_DIR=SAVED_MODEL_DIR

TRAINING_BUCKET_NAME="mynetworksecurity"
PREDICTION_BUCKET_NAME="my-network-datasource"
PREDICTION_DIR="prediction"

