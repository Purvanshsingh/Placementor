import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn




class Response(BaseModel):
    _10th : float
    _12th: float
    medium: str
    year : int
    backlog : int
    aggregate: float
    sem1 : float
    sem2: float
    sem3: float
    sem4: float
    sem5: float
    sem6: float
    sem7: float
    sem8: float
    skills: str



app = FastAPI()
data = pd.read_excel('Placed students_2019 Batch.xls')
data = data['Placed in Company (Name)'].unique()


@app.get('/')
def index():
    return "Please make POST request @placementor"


@app.post('/placementor/')
async def index_route(word: Response):
    predicted_company = np.random.choice(data)
    return predicted_company

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)