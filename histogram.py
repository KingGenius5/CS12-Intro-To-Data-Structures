import sys

def read_file(file_name):
    #Read in file
    with open(file_name, 'r') as f:
        words = f.read().split()

    #Strip words of special characters

    word_list = []
    for word in words:
        word = word.rstrip()
        word_list.append(word)

    return word_list

#dictionary
def histogram_dictonary(words):
    word_histogram = dict()

    #Look up and increment word
    for word in words:
        word_histogram[word] = word_histogram.get(word, 0) + 1

    return word_histogram


def histogram_list_of_lists(words):
    word_histogram = list()

    for word in words:
        for item in word_histogram:
            #Check if item already in list
            if item[0] == word:
                item[1] += 1
                break

        #add item to list if it does not exist
        else:
            word_histogram.append([word, 1])

    return word_histogram

def unique_words(word_histogram):
    uniw = set(word_histogram)
    return len(uniw)

#def frequency(words, word_histogram):



if __name__ == "__main__":

    words = read_file("sample.txt")
    
    print(histogram_dictonary(words))
    print(histogram_list_of_lists(words))
    print(unique_words(words))



'''
filename = "sample.txt"
lines = open(filename, "r")

word_histogram = {}

for word in lines:
  
  word = word.rstrip()
  #TODO: add code to increase the count in the histogram for the given word
  
  if word not in word_histogram.keys():
      word_histogram[word]=1

  else:
      word_count_value = word_histogram.get(word)
      word_count_value +=1
      word_histogram[word] = word_count_value


  #Another way but shorter
  word_histogram[word] = word_histogram.get(word, 0) + 1
  '''