def gen(n):
    for i in range(n,0,-1):
        yield i
n = int(input())
gener = gen(n)
print(*gener)