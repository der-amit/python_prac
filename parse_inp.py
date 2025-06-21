#Parse input to numeric lists

def read_integers():
    inp = input()
    list = inp.split(",")
   # return list

    int_list = []
    for num in list:
        int_list.append(int(num))
    
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())