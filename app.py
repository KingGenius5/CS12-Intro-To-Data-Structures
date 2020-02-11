from flask import Flask
from sample import *

app = Flask(__name__)

@app.route('/')
def main_tweet_page():
    
    words = read_file('fish.txt')
    hist = histogram_dictonary(words)
    token_count = len(words)
    sent = sentence_gen(8, token_count, hist)

    return sent