#Take a user input and sort it

def sort_words():
    inp = input()
    split_list = inp.split(",")
    mylist = []
    for word in split_list:
        mylist.append(str(word))
       
    mylist.sort()
    return mylist
    
    
print(sort_words())