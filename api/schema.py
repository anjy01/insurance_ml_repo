from pydantic import BaseModel,Field
from typing import Literal


# create the object for request payload
# 'age', 'sex', 'bmi', 'children', 'smoker', 'region'
class UserRequest(BaseModel):
    age: int = Field(..., description="Age of the client.",
                     examples=[35], ge = 1, le=90)
    sex: Literal['male','female'] = Field(..., description="gender of the client.",
                     examples=["female"])
    bmi: float = Field(..., description="body mass index of the client.",
                     examples=[25.3], ge = 6.7, le=60)
    children: int = Field(..., description="No of children the client has.",
                     examples=[3], ge = 0, le=15)
    smoker: Literal['yes','no'] = Field(..., description="Does the client smoke?.",
                     examples=["yes"])
    region: Literal['northeast','northwest',
                    'southeast','southwest'] = Field(..., description="what is the zone of the client.",
                     examples=["northeast"])
    

# create the response object
class ModelResponse(BaseModel):
    message: str = Field(..., 
                         examples=["This user's charges is predicted to be $5.67"])
    
    