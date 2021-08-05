import fastapi
from typing import Optional

app = fastapi.FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/{greet}")
def greet_something(greet: str, something: Optional[str] = "World"):
    return {greet: something}
