import sys
import random as r

filename = "/Users/mtifak/Desktop/dev/Term-3/CS-1.2/Tweet-Generator/words.txt"

my_file = open(filename, "r") #this just opens the file, how to get the stuff in the file
lines = my_file.readlines()#this reads the lines and stores them in lines
my_file.close()

print(lines)