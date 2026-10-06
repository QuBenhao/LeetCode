# [Python] Avoid precision issues with multiplication or the Euclidean algorithm

> Author: Benhao
> Date: 2021-06-24
> Upvotes: 15
> Tags: Python, Python3

---

### Approach
Use multiplication on pairwise differences to check whether points lie on the same line. (This requires an o(n^3) brute-force check.)
Count points on the same kx+b line with a hash table to remove one loop. (Use the Euclidean algorithm to avoid division precision issues.)
Since the line always passes through the point chosen by the outer loop, only its slope is needed. (One point and one slope determine a line.)

### Code

```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Three collinear points have equal slopes
        # y2 - y1 = k * (x2 - x1), y3 - y2 = k * (x3 - x2)
        # (y2 - y1) * (x3 - x2) = (y3 - y2) * (x2 - x1)
        
        explored = set()
        ans = 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                curr = 2
                dx,dy = points[j][0] - points[i][0],points[j][1] - points[i][1]
                for k in range(j+1, len(points)):
                    if (i,j) in explored or (i,k) in explored or (j,k) in explored:
                        continue
                    if dy * (points[k][0] - points[j][0]) == (points[k][1] - points[j][1]) * dx:
                        curr += 1
                        explored.add((j,k))
                        explored.add((i,k))
                ans = max(ans, curr)
        return ans
```

```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(m, n):
            return m if not n else gcd(n, m%n)
        
        def getslope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            
            if dx == 0: return (p1[0], 0)
            if dy == 0: return (0, p1[1])
            
            d = gcd(dx, dy)
            return (dx//d, dy//d)
        
        res = 0
        for i in range(len(points)):
            d = defaultdict(lambda:0)
            same, maxi = 1, 0
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1 == p2:
                    same += 1
                else:
                    slope = getslope(p1, p2)
                    d[slope] += 1
                    maxi = max(maxi, d[slope])
            res = max(res, same + maxi)
            
        return res
```
Store the result of high-precision division as a string
```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def hdiv(dividend, divisor, accuracy):
            '''
            Purpose: perform high-precision division
            Parameters:
                dividend: the dividend
                divisor: the divisor
                accuracy: division precision
            Returns: the result as a string
            '''
            # Define a string to store the result
            res = ''

            # Define a variable to track the sign
            isNegative = False

            # Determine the sign
            if dividend < 0 and divisor > 0:
                dividend = abs(dividend)
                isNegative = True
            elif divisor < 0 and dividend > 0:
                divisor = abs(divisor)
                isNegative = True

            # Add the sign to the result
            if isNegative:
                res += '-'

            # Calculate the integer part
            integer = round(dividend // divisor)

            # Append the calculated value to the result
            res += str(integer) + '.'

            # Calculate the remainder
            remainder = dividend % divisor

            # Calculate the fractional part
            for i in range(accuracy):
                dividend = remainder * 10
                res += str(round(dividend // divisor))
                remainder = dividend % divisor

            return res

        # k = (y2 - y1) / (x2 - x1), b = y - k * x
        ans = 1
        for i in range(len(points)):
            d = Counter()
            for j in range(i+1, len(points)):
                if not points[j][0] - points[i][0]:
                    k = inf
                else:
                    k = hdiv(points[j][1] - points[i][1],points[j][0] - points[i][0],10)
                d[k] += 1
            if d:
                ans = max(ans, max(d.values()) + 1)
        return ans
```
