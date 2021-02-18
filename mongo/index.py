from pymongo import MongoClient
import dnspython

client = MongoClient("mongodb+srv://leocrapart:Dupr0pnet@cluster0.xbfcm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["voc_tool"]

colWords = db["words"]

## get   

def getAllWords():
    words = colWords.find()
    wordList = list(map(lambda x: x["word"], words))
    return wordList

def getByWord(word):
    query = {"word": word}
    wordItem = colWords.find_one(query)
    print(f"wordItem => {wordItem}")
    
    return {"word": wordItem["word"]}

def getOneWord():
    wordItem = colWords.find_one()
    return wordItem

## insert

def insertWord(wordItem):
    print(wordItem.dict())
    res = colWords.insert_one(wordItem.dict())
    insertedId = str(res.inserted_id)
    return insertedId

## update


def deleteWord(word):
    query = {
        "word": word
    }
    print(query)
    res = colWords.delete_many(query)
    print(res)
    return res.deleted_count

## test

    
    
    
    
    
    
    
    
    