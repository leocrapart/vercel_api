from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
	return {
		"weeeelcome": "its working "
	}