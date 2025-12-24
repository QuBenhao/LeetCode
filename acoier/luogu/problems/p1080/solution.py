n = int(input())
a, b = map(int, input().split())
coins = []
for _ in range(n):
    ca, cb = map(int, input().split())
    coins.append([ca, cb])
coins.sort(key=lambda x: x[0] * x[1])
ans = 0
for ca, cb in coins:
    if (cur := a // cb) > ans:
        ans = cur
    a *= ca
print(ans)