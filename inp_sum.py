#Taking user inputs and returning sum

def add_nums():
    inp = input()
    list = inp.split(",")
    
    num_list = []
    for num in list:
        k = int(num)
        num_list.append(k)
    return sum(num_list)
    

print(add_nums())
print(add_nums())
print(add_nums())
print(add_nums())