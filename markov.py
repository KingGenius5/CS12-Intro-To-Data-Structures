from dictogram import Dictogram
from histogram import read_word_file
import random
import string


'''
Note: Currently using this version of my own previous built-up Markov chains to get the
project off the ground. Ran into some errors with the MarkovChain Class, will revisit and fix class later
on. This works just as well (prints the walks with capital letters and grammar) but is function-based rather than class-based.
'''

def higher_order(word_list, new_words, order=2):
    storage_dict = dict()

    key_words = new_words.split()
    if len(key_words) != order:
        return "Length of input words does not equal order"

    words = []
    next_words = []
    next_pairs = []

    for i in range(len(word_list) - 1):
        words.clear()
        for j in range(order):
            if i < (len(word_list) - order):
                words.append(word_list[i + j])
        if key_words == words:
            next_words.clear()
            for j in range(order):
                next_words.append(word_list[i + (j + 1)])
            next_words_str = " ".join(next_words)
            next_pairs.append(next_words_str)

    storage_dict[new_words] = Dictogram(next_pairs)
    return storage_dict

def order_sample(word_list, order=2):
    histogram = Dictogram(word_list)
    next_words = []

    # sample a random word from histogram
    next_word_str = histogram.sample()
    # find all the words that come after 
    chain = new_chain(word_list, next_word_str)
    # append both words to a list
    next_words.append(next_word_str)

    for i in range(order - 1):
        if len(chain) > 0:
            next_word_str = chain.sample()
            next_words.append(next_word_str)
            chain = new_chain(word_list, next_word_str)

    # join the words into a string and assign to a variable
    words_str = " ".join(next_words)
    return words_str

def higher_order_walk(word_list, length, order=2):
    sentence = []
    next_words_list = []
    
    words_str = order_sample(word_list, order)
    # append both words to the sentence
    sentence.append(words_str)

    # repeat until length of sentence == length input
    for i in range(length - order):
        # make sure next_words_list is empty
        next_words_list.clear()
        # get the list of pairs that comes after the previous pair
        chain = higher_order(word_list, words_str, order)
        # if the chain isn't empty
        if len(chain[words_str]) > 0:
            # sample the value in the chain, which is a dictogram
            words_str = chain[words_str].sample()
            # add both words individually to next_words_list
            next_words_list = words_str.split()
            # only append the second word to the sentence
            sentence.append(next_words_list[order - 1])

    return create_sentence(sentence)


def new_chain(word_list, word):
    
    chain_list = []
    for i in range(len(word_list) - 1):
        if word == word_list[i]:
            chain_list.append(word_list[i + 1])

    chain = Dictogram(chain_list)
    return chain


def walk(word_list, length):
    
    sentence = []
    histogram = Dictogram(word_list)
    next_word = histogram.sample()
    sentence.append(next_word)
    for i in range(length - 1):
        chain = new_chain(word_list, next_word)
        if len(chain) > 0:
            next_word = chain.sample()
            sentence.append(next_word)

    return sentence


def create_sentence(words):
    
    words[0] = words[0].capitalize()
    last_word = words[len(words) - 1]
    last_char = last_word[len(last_word) - 1]
    formatted_sentence = ' '.join(words)
    if last_char in string.punctuation:
        formatted_sentence = formatted_sentence[:-1]
    formatted_sentence = formatted_sentence + "."
    return formatted_sentence


if __name__ == "__main__":
    words = read_word_file('manifesto.txt')
    #word_list = words.split()
    print(higher_order_walk(words, 40))


'''

class MarkovChain:

    def __init__(self, word_list):


        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        #TODO: generate a sentence num_words long using the markov chain
        word = self.first_word
        for i in range(num_words):
            dictogram = self.markov_chain[word]
            word = dictogram.sample()

        return word

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))


'''