from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 
from schema import UserRequest, ModelResponse
from utils import predict_charges

# create an app instance
app = FastAPI(
    title = "Insurance application"
)

# define the root endpoint.
@app.get("/", tags=["test"])
def root():
    return {"message": "we are live!!"}

# an endpoint that greets people
@app.post("/greet/", tags=["test"])
def greet(name: str, year_birth: int):
    age = 2025 - year_birth
    return {
        "greeting": f"Hi {name} how are you?",
        "age": f"Wow, you are {age} years old"
    }
@app.post('/get_charges',response_model=ModelResponse,
          tags = ["ml-endpoints"])
def predict(payload: UserRequest):
    data = payload.model_dump()
    prediction = predict_charges(**data)

    return ModelResponse(
        message= prediction
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, host = "localhost", reload = True)