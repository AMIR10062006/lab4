def gen(a,b):
    for i in range(a,b+1):
        yield i**2
a = int(input())
b = int(input())
squares = gen(a,b)
print(*squares)