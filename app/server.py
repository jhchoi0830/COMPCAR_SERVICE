# import modules
from fastapi import FastAPI, HTTPException
# import model


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
