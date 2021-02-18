from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import mongo.index as mongo

app = FastAPI()

class WordItem(BaseModel):
    word: str


@app.get("/")
def home():
	return {
		"weeeelcome": "its working 2"
	}


@app.get("/words")
def getAllWords():
    wordList = mongo.getAllWords()
    return {
        "words": wordList
    }

@app.post("/words")
def insertWord(wordItem: WordItem):
    insertedId = mongo.insertWord(wordItem)
    return {
        "_id": insertedId
    }

@app.delete("/words/{word}")
def deleteWord(word: str):

    deletedCount = mongo.deleteWord(word)
    return {"deletedCount": deletedCount}