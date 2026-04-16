# [Python] 使用乘法 or 辗转相除法 避免精度问题

> Author: Benhao
> Date: 2021-06-24
> Upvotes: 15
> Tags: Python, Python3

---

### 解题思路
两两之差用乘法判断在不在一条直线上。(但是需要o(n^3)暴力判断)
使用哈希表统计同一kx+b的个数可以少一层循环。(需要使用辗转相除法避免除法精度问题)
因为直线总是以经过外层循环的点，所以取一个斜率即可(一个点和一个斜率确定一条直线)

### 代码

```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 三点在一条直线上时,斜率相等
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
使用字符串存储高精度除法结果
```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def hdiv(dividend, divisor, accuracy):
            '''
            功能: 完成高精度的除法
            参数:
                dividend: 被除数
                divisor: 除数
                accuracy: 除法精度
            返回: 计算结果(字符串)
            '''
            # 定义存储结果的字符串
            res = ''

            # 定义保存正负数的变量
            isNegative = False

            # 确定正负号
            if dividend < 0 and divisor > 0:
                dividend = abs(dividend)
                isNegative = True
            elif divisor < 0 and dividend > 0:
                divisor = abs(divisor)
                isNegative = True

            # 在结果添加正负号
            if isNegative:
                res += '-'

            # 计算整数部分
            integer = round(dividend // divisor)

            # 将结果添加入结果
            res += str(integer) + '.'

            # 计算余数
            remainder = dividend % divisor

            # 计算小数部分
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