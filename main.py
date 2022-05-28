# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from pydoc import text


def read_file_content(filename):
    # [assignment] Add your code here 

    filename = open("./story.txt")
    line = filename.readline()   
        
    while line:
        line = filename.readline()
        print(line.strip()) 

    filename.read()

    return filename



from collections import Counter

def count_words(str):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    with open(str) as f:
         return Counter(f.read().split())

print("Number of words in the file :",count_words("./story.txt"))