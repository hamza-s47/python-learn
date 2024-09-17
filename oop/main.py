def func(n):
    return lambda x : n*x

one = func(4)
print(one(2))


sum = lambda a, b, c : a+b+c

print(sum(2,4,6))
