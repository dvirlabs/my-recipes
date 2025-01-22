from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db_utils import *


CORSMiddleware = [
    CORSMiddleware(
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_recipes")
def get_recipes():
    return get_all_recipes()




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)