def rotLeft(a, d):
    return a[d:] + a[:d]

n, d = [int(x) for x in input().split()]
a = list(map(int, input().split()))
print(*rotLeft(a, d), sep = " ")
