from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

class CorrectorModel:

    def __init__(self) -> None:
        self.models = {
            'en': self._init_english_corrector(),
            'pt': None
        }
        
    def _init_english_corrector(self):
        tokenizer = AutoTokenizer.from_pretrained(
            "leslyarun/grammatical-error-correction")
        model = AutoModelForSeq2SeqLM.from_pretrained(
            "leslyarun/grammatical-error-correction")
        
        return pipeline("text2text-generation", model=model, 
                        tokenizer=tokenizer)


    def correct(self, text: str, language: str):
        output = self.models[language]("grammar: " + text)
        return output[0]["generated_text"]
    

model = CorrectorModel()
def get_model():
    return model