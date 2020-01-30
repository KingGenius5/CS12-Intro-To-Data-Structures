import sys

def read_word_file(file_name):
    with open(file_name, 'r') as f:
        words = f.read().split()
    return words


def histogram_dict(word_list):
    #Using dictionaries
    histogram = {}
    for word in word_list:
        word = word.strip('?!,.-*[]:').lower()
        histogram[word] = histogram.get(word, 0) + 1 
    
    return histogram


def histogram_list_of_lists(word_list):
    #Using lists
    histogram = []

    for word in words:
        for item in histogram:
            #Check if item already in list
            if item[0] == word:
                item[1] += 1
                break

        #add item to list if it does not exist
        else:
            histogram.append([word, 1])

    return histogram

    
def unique_words(histogram):

    '''
    uniw = set(histogram)
    return len(uniw)

    '''
    return len(histogram)

def frequency(histogram, word):
    
    if word in histogram.keys():
        return histogram[word]
    else:
        return 0


if __name__ == "__main__":

    words = read_word_file("sample.txt")
    word_list = read_word_file("sample.txt")
    histogram = histogram_dict(word_list)
    
    print(histogram_dict(words))
    print(histogram_list_of_lists(words))
    print(unique_words(histogram))
    print(frequency(histogram, "espresso"))


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
