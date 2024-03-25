# task2
## Purpose
This is a simple application that predicts revenue based on a json data of ads. The model was trained in [Colab Notebook](https://colab.research.google.com/drive/1zTPfEcyrGzFCvKJDDOZyA23XMB1akeDd?usp=sharing).
## Environment variables
DATA_PATH -> Set the path where is the json ad file. It'll default to the project data
## Json_data
For the prediction to be possible, we need 3 keys: total_impressions, viewable_impressions and measurable_impressions per record
## Output
The output will be saved in a json on a folder called predictions and the file will be called predictions.json with will contain all the record + the total_revenue prediction per record
## Running local
To run the prediction, just clone this repo, go to root project folder and type python3 src/main
## Running docker
To run the prediction, just build and image and run or pull image from [Docker hub](https://hub.docker.com/r/andonokar/task2).
To pull the image:
docker pull andonokar/task2
It'll print the json data in a python dictionary just for visualization