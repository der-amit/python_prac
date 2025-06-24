#Creating a  dictionary by taking two lists containing keys and values
def group_names_scores(names, scores):
    mydict = {}
    for n, s in zip(names, scores):
        mydict[n] = s
    return mydict
        

print(group_names_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))