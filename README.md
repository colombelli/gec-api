# gec-api

An API for the grammatical error correction NLP task, using HuggingFace and FastAPI.

### start server
    
    $ chmod +x bin/start_server
    $ bin/start_server

#### httpie usage:
    
    $ http http://127.0.0.1:8000/correct text="please, correct the spelling of this text for me"