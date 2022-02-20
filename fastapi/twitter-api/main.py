# Python

# Pydantic

# FastAPI
from fastapi import FastAPI

# My imports


app = FastAPI()

@app.get(
    path='/',
    tags=['Configuration']
)
def home():
    return {'Twitter API': 'Working'}