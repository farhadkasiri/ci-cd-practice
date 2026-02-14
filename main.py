from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add_endpoint(a: int, b: int):
    return {"result": a + b}

@app.get("/subtract")
def subtract_endpoint(a: int, b: int):
    return {"result": a - b}
