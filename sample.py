import sys
import random

'''
text = 'one fish two fish red fish blue fish'
word_counts = {'one': 1, 'fish': 4, 'two': 1,
               'red': 1, 'blue': 1}
'''

def read_file(file_name):
    #Read in file
    with open(file_name, 'r') as f:
        words = f.read().split()

    #Strip words of special characters
    for word in words:
        word = word.strip(".@'/")

    return words

def histogram_dictonary(words):
    histogram = dict()

    #Look up and increment word
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

def sample_by_frequency(histogram):

    # TODO: select a word based on frequency
    #how can we sample words using observed frequencies?