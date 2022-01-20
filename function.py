def most_frequent(string):
    d = dict()
    for i in sorted(string,reverse=True):
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print( most_frequent('mississippi'))


