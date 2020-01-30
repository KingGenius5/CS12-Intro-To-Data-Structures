import random
import sys

def read_file():
    words_list = list()
    with open('/usr/share/dict/words', 'r') as f:
        words_list = f.read().split('\n')

    return words_list

def select_words(count, list_of_words):
    sentence = list()

    while count > 0:
        index = random.randint(0, len(words_list) - 1)

        sentence.append(list_of_words[index])
        count -= 1

    return ' '.join(sentence)



if __name__ == "__main__":
    
    words_list = read_file()

    count = int(sys.argv[1])

    print(select_words(count, words_list))