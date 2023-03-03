from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class CorrectorResponse(BaseModel):
    text: str


@app.post("/correct", response_model=CorrectorResponse)
def correct(request: TextRequest):
    return CorrectorResponse(
        text="Yes, that's correct."
    )