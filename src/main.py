from fastapi import FastAPI, HTTPException
from data import IrisData, IrisResponse
from predict import predict

# Create the FastAPI app instance
# This is the core object that handles all incoming requests
app = FastAPI()

# ─────────────────────────────────────────
# Endpoint 1: Health Check
# ─────────────────────────────────────────
# What: A simple GET request to "/" that confirms the API is alive
# Why: Always useful to have a health check — lets you quickly verify
#      the server is running without doing a full prediction
# @app.get means this responds to GET requests (just visiting a URL)
@app.get("/")
async def root():
    return {"message": "Iris Prediction API is running!"}

# ─────────────────────────────────────────
# Endpoint 2: Prediction
# ─────────────────────────────────────────
# What: Accepts flower measurements, returns predicted species number
# Why POST: Because we are SENDING data (measurements) to the server
#           GET is for retrieving, POST is for sending data
# data: IrisData → FastAPI automatically validates the incoming data
# response_model=IrisResponse → FastAPI formats the output correctly
@app.post("/predict", response_model=IrisResponse)
async def predict_species(data: IrisData):
    try:
        result = predict(data)                 # call our predict function
        return IrisResponse(response=result)   # wrap result in response model
    except Exception as e:
        # If anything goes wrong, return a proper error message
        # instead of crashing the whole server
        # status_code=500 means "Internal Server Error"
        raise HTTPException(status_code=500, detail=str(e))