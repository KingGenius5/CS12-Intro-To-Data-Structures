from random import randint

filename = "/Users/mtifak/Desktop/dev/Term-3/CS-1.2/Tweet-Generator/words.txt"

my_file = open(filename, "r") #this just opens the file, how to get the stuff in the file


lines = my_file.readlines()#this reads the lines and stores them in lines

my_file.close()#the lines will still print because they were stored on the variable lines

print(lines)

#How do you approach randomly accessing items in a list?
random_index = randint(0, len(lines)-1)#since lists start at 0, subtract 1 at the end
print(lines[random_index])