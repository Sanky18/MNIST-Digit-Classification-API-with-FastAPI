# MNIST Digit Classification API with FastAPI

## Overview
This repository contains a FastAPI module that exposes a REST API for digit classification using the MNIST dataset. Users can upload images of handwritten digits, and the API will predict the digit using a pre-trained model.

## Features
- **Model Loading**: Load a pre-trained MNIST digit classification model from a specified path on the disk.
- **Digit Prediction**: Predict the digit in an uploaded image using the loaded model.
- **Image Formatting**: Resize uploaded images to 28x28 grayscale and create a serialized array of 784 elements for prediction.
- **API Endpoint**: Expose a POST endpoint at `/predict` to accept image uploads, preprocess the data, and return the predicted digit.
- **Swagger UI Integration**: Accessible via `<api endpoint>/docs`, allowing users to test the API using Swagger UI.
- **Performance Evaluation**: Test the API with hand-drawn digit images and record observations.

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
4. **Access the API at the specified endpoint.**

## Project Structure
      ├───app
      │   ├───__pycache__
      │   ├───digit_predictor.py
      │   ├───image_formatter.py
      │   └───main.py
      ├───models
      ├───scripts
      │   └───train_best_model.py
      └───tests



## Usage

1. **Load the Pre-trained Model:**
   - Use the `model_loader.py` module to load the pre-trained MNIST digit classification model.

2. **Start the FastAPI Server:**
   - Run `main.py` to start the FastAPI server.

3. **Test the API:**
   - Use Swagger UI or Postman to test the API endpoint (`/predict`).

4. **Upload Images:**
   - Upload images of handwritten digits to receive predictions.

## Performance Evaluation

Record observations by conducting experiments with hand-drawn digit images. Each experiment should involve:

- Drawing a digit using tools like MS Paint or equivalent.
- Uploading the digit image to the API.
- Comparing the predicted digit with the ground truth.
- Recording the results in a video format for each experiment.

## Experiment Demonstrations

We have conducted 10 experiments, each corresponding to a hand-drawn digit created in MS Paint. These experiments were evaluated by uploading the images to the FastAPI.















