from pydantic import BaseModel

# This defines what the USER SENDS to the API (input)
# All 4 measurements of the iris flower — all must be decimal numbers (float)
# If someone sends a string like "hello" instead of 1.4, FastAPI auto-rejects it
class IrisData(BaseModel):
    petal_length: float   # e.g. 1.4
    sepal_length: float   # e.g. 5.1
    petal_width: float    # e.g. 0.2
    sepal_width: float    # e.g. 3.5

# This defines what the API SENDS BACK to the user (output)
# Just one integer: 0 = setosa, 1 = versicolor, 2 = virginica
class IrisResponse(BaseModel):
    response: int