import sys
import random
import time
start_time = time.time()

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
    histogram = {}

    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

#create the sample list
def sample_list(histogram):
    words_list = []

    for key, value in histogram.items():
        #add values to new list
        for i in range(value):
            words_list.append(key)

    return words_list

def sample_by_frequency(count, words_list):

    # TODO: select a word based on frequency
    #how can we sample words using observed frequencies?

    list_count = []
    histogram_count = {}
    
    for i in range(count):
        list_count.append(random.choice(words_list))

    for word in list_count:
        histogram_count[word] = histogram_count.get(word, 0) + 1

    return histogram_count

def sentence_gen(count, token_count, histogram):

    #get total number of words from selection
    sentence = ""

    while count > 0:
        #choose a random number in that range.
        rand_value = random.randint(0, token_count - 1)

        #keeps track of value
        total_count = 0

        #loop through list and add values to total count
        for key, value in histogram.items():
            
            if rand_value <= total_count:
                sentence += f" {key}"
                break

            total_count += value
        
        count -= 1

    return sentence
    

if __name__ == "__main__":

    file_name = sys.argv[1]
    words = read_file(file_name)

    hist = histogram_dictonary(words)
    words_list = sample_list(hist)

    print(sample_by_frequency(10000, words_list))

    token_count = len(words)
    sent = sentence_gen(8, token_count, hist)
    print(sent)
    #Thanks to Ninja for this.
    print(f"--{time.time() - start_time} secounds --")
