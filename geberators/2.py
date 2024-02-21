def gen(n):
    for i in range(0,n+1,2):
        yield i
N = int(input())
print(*gen(N),sep=";")
