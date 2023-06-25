from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/')
def home():
    return {"key": "value"}
