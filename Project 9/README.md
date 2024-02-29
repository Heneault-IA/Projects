# Project 9 : Big Data Environement : Images Featurisation

## Data Needeed
https://www.kaggle.com/datasets/moltean/fruits to download in the "Data/fruits-360_dataset/fruits-360/Training" folder for the Technology Watch

## Librairies Needed
wheel
pillow
pandas==1.2.5
pyarrow
boto3
fsspec
tensorflow==2.11.0

## Scripts

"bootstrap-emr.sh" : initiation file for the EMR cluster.
"notebook_persitence.json" : parameters file for the EMR cluster. Used to have a persitence in the file jupyter we'll create on JupyterHub

## Notebooks

"Pyspark_Notebook.ipynb" : Notebook used in the JupyterHub of our EMR cluster.

"Création_Training_set.ipynb" : create the training dataset to test our featurisation.

## Results

paquet's files that result from our notebook with the featurised data.
