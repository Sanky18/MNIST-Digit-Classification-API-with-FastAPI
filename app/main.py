from fastapi import FastAPI, UploadFile, File, HTTPException
from model_loader import load_model
from digit_predictor import predict_digit
from image_formatter import format_image


app = FastAPI()
loaded_model = 0
ALLOWED_IMAGE_FORMATS = ['png', 'jpeg', 'jpg']  # Allowed image formats

@app.on_event("startup")
async def startup_event():
    global loaded_model
    # Load model on startup
    model_path = "A:\Jan-May 2024\CS5830-Big Data Laboratory\Assignment-6\models\mnist_model.h5"
    loaded_model = load_model(model_path)



@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    # Check if the uploaded file is of allowed image format
    if not any(file.filename.lower().endswith(ext) for ext in ALLOWED_IMAGE_FORMATS):
        raise HTTPException(status_code=400, detail="Please upload images of format PNG/JPEG")
    
    # Read the bytes from the uploaded image
    contents = await file.read()

    # Convert the image bytes to a 1D array of 784 elements
    data_point = format_image(contents)

    # Predict the digit and its confidence score
    digit, confidence_score = predict_digit(loaded_model, [data_point])
    # Return the prediction and confidence score
    return {"digit": digit, "confidence_score": float(confidence_score)}  