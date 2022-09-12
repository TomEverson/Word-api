from fastapi import FastAPI
import text

app = FastAPI()

@app.get('/{words}')
def get(words):
    word = text.word.load_words(words)
    return word 