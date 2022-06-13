# C22-PS283: Machine Learning Path
## About Calistung
Calistung: Baca, Tulis, Hitung is an application that provide educational features to help children learn to write, read, and count.

## Technology Used for ML Repo
   - [Tensorflow](https://www.tensorflow.org/)
   - [Python](https://www.python.org/)
   - [FastAPI](https://fastapi.tiangolo.com/)

## Dataset Resources
   - [Kaggle A-Z Handwritten](https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format)
   - MNIST Dataset
   - [Additional Handwritten Character](https://drive.google.com/drive/folders/1dZ4tDnD2ju0sAffCIKa0dh4HpGrMSt2r?usp=sharing)

## Notebooks
[Image Classification Folder](https://drive.google.com/drive/folders/1Q3EAY9WIJNiLmQbbTwH0CXu5ZroIM9Id?usp=sharing)

## API URL Created by CC
[Calistung](https://calistung.uc.r.appspot.com/) 

## Installing FastAPI App
  - Download the repo/clone it. Make it available on your device
  - Open terminal and go to the project's directory
  - Type `python -m venv env` and press enter (create virtual environment)
  - For Windows user, type `env\Scripts\activate`. For Linux, type `source ./env/bin/activate` (accessing the virtual environment)
  - Type `pip install -r requirements.txt` (installing the requirements)
  - Serve the app by typing `uvicorn main:app --reload`
  - It will run on `http://127.0.0.1:8000`

## Character Recognition Endpoint

| Endpoint | Method |           Body Sent          |                 Description                |
|:--------:|:------:|:-----------------------------------:|:------------------------------------------:|
|     /    |   GET  |                 None                |            HTTP GET REQUEST Testing Endpoint            |
|     /predict    |  POST  |                 Image file:  'Image'               | HTTP POST REQUEST Prediction Endpoint |

## How to predict image with Postman
  - Open Postman App
  - Enter URL request bar with `http://127.0.0.1:8000/predict`
  - Select method POST
  - Go to Body tab and select form-data
  - Change key from form-data with file, with name `Image`
  - Input the image that you want predict as a value of the key
  - Send the request, or
  - Simply access `http://127.0.0.1:8000/docs` and execute the `predict` endpoint

## Helpful References
  - [Adding own data to MNIST](https://medium.com/@ashok.tankala/build-the-mnist-model-with-your-own-handwritten-digits-using-tensorflow-keras-and-python-f8ec9f871fd3)
  - [Padding Same vs Valid](https://www.pico.net/kb/what-is-the-difference-between-same-and-valid-padding-in-tf-nn-max-pool-of-tensorflow)
