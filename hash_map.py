# Hashmap basics

mydict = {}

'''Insertion: Insert a key-value pair into the hash map.'''
mydict['a'] = 1
print(mydict)

'''Access: Access the value associated with a key.'''

mydict = {'b':2}    # Note that this replaces mydict, so a=1 is replace with b = 2 as we used the = operator
print(mydict['a'])

mydict['a'] = 1
print(mydict)

''' Or you can assign multiple key value pairs'''

mydict = {'a':1, 'b':2}
print(mydict)


''' delete a key value pair from the hashmap'''

del mydict['a']
print(mydict)

#>>> print(mydict)
#{'b': 2}

mydict['a'] = 1
print(mydict)

#>>> print(mydict)
#{'b': 2, 'a': 1}

mydict.pop('a')     # Note that this returns the value(1 here) associated with the key('a' here)
print(mydict)

''' Look up if a key exists in a hashmap'''

print(f'{'a' in mydict}')   # Always check using the key and not the value
print(f'{'b' in mydict}')
