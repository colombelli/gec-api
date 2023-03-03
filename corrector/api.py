from fastapi import FastAPI, Depends
from pydantic import BaseModel
from .CorrectorModel import CorrectorModel, get_model

app = FastAPI()

class TextRequest(BaseModel):
    text: str
    language: str

class CorrectorResponse(BaseModel):
    text: str


@app.post("/correct", response_model=CorrectorResponse)
def correct(request: TextRequest, model: CorrectorModel = Depends(get_model)):
    corrected_text = model.correct(request.text, request.language)
    return CorrectorResponse(
        text=corrected_text
    )