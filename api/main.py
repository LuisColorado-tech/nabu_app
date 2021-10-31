from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Root path operation function
@app.get("/")
def read_root():
    return {"Welcome to NABU system application"}
