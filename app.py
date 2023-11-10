from fastapi import FastAPI

app = FastAPI()

@app.put("/")
def execute(name: str):
	return f"Hello, {name}!Hello, {name}!"