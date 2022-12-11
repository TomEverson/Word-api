from fastapi import FastAPI
import text

app = FastAPI()

@app.get('/{words}')
def get(words):
    words = text.word.load_words(words)
    return words