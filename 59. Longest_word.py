def longest(string):
    length = 0
    w =''
    for word in data:
        if(len(word)>length):
            length = len(word)
            w = word
    return(length,w)
string = input("Enter the string: ")
data = string.split()
l,w = longest(string)
print("Longest word is",w,"and its length is",l)
