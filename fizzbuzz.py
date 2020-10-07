def fizzbuzz():
    res = []
    for i in range(100):
        i = i+1
        if i % 3 == 0 and i % 5 == 0:
            res.append('Fizzbuzz')
        elif i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(i)
    return res

print(fizzbuzz())