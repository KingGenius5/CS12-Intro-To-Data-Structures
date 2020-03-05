from flask import Flask, render_template, request, redirect, url_for
from sample import *
from markov import *
import random
from dictogram import Dictogram
from histogram import *

app = Flask(__name__)

@app.route('/')
def main_tweet_page():
    
    words = read_file('manifesto.txt')
    sent = higher_order_walk(words, 40)

    return render_template('index.html', sentence=sent)