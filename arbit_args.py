def concat(*args):
    result = ''
    
    for arg in args:
        result = result + ' ' + arg
    return result

print(concat('This','is', 'a', 'test'))