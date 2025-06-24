#Dictionary looping

def get_dict_keys(age_dict):
    keys = []
    for key in age_dict.keys():
        keys.append(key)
    return keys

def get_dict_values(age_dict):
    values = []
    for key in age_dict.keys():
        values.append(age_dict[key])
    return values
    
    
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))