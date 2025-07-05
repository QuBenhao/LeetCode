"""
D. CGCDSSQ
time limit per test2 seconds
memory limit per test256 megabytes
Given a sequence of integers a1,...,an and q queries x1,...,xq on it. For each query xi you have to count the number of pairs (l,r) such that 1≤l≤r≤n and gcd(al,al+1,...,ar)=xi.

 is a greatest common divisor of v1,v2,...,vn, that is equal to a largest positive integer that divides all vi.

Input
The first line of the input contains integer n, (1≤n≤10^5), denoting the length of the sequence. The next line contains n space separated integers a1,...,an, (1≤ai≤10^9).

The third line of the input contains integer q, (1≤q≤3×10^5), denoting the number of queries. Then follows q lines, each contain an integer xi, (1≤xi≤10^9).

Output
For each query print the result in a separate line.
"""

from math import gcd
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

g = []
cnts = defaultdict(int)
for i, x in enumerate(nums):
    g.append([x, i])

    j = 0
    left = 0
    for p in g:
        p[0] = gcd(p[0], x)
        if g[j][0] != p[0]:
            j += 1
            g[j] = p
        else:
            g[j][1] = p[1]
        cnts[p[0]] += p[1] - left + 1
        left = p[1] + 1
    del g[j + 1:]

q = int(input())
for _ in range(q):
    x = int(input())
    print(cnts[x])
