input = input("Please enter a string: ")
def most_frequent(string):
    import operator
    d = {}
    
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        d_lower = {k.lower(): v for k, v in d.items()}
        d_sorted = dict(sorted(d.items(), key = operator.itemgetter(1),reverse = True))
        
    return d_sorted


print(most_frequent(input))
