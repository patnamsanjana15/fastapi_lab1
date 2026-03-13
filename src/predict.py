import pickle
import numpy as np

# Load the saved model from disk
# "rb" means "read binary" — we're reading the binary .pkl file
# Why a function? So we can call load_model() anytime we need the model
def load_model():
    with open("../model/iris_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# Takes flower data as input, runs it through the model, returns prediction
def predict(data):
    model = load_model()

    # The model expects data in a 2D array format: [[val1, val2, val3, val4]]
    # np.array converts our input data into that exact format
    input_array = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    # model.predict() returns an array like [0]
    # We take [0] to get just the number 0, then convert to Python int
    prediction = model.predict(input_array)
    return int(prediction[0])