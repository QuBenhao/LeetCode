# [Python] 26进制

> Author: Benhao
> Date: 2021-06-28
> Upvotes: 11
> Tags: Python, Python3

---

### 解题思路
本质上其实我们在用字母来写一个26进制,A代表1,B代表2,....Z代表26。

基础知识
> 10进制数字$n$转换为k进制时，可以通过辗转相除依次计算从右边开始的每一位。
因为最终我们要找到$n = a_{0} * k^m + a_{1} * k^{m-1} + \ldots + a_{m} * 1$,
所以$a_m = n$%$k$ (前面的所有都乘了k的某个次方所以整除k)。
然后 $(n - a_m) // k$ 就得到了 $a_0 * k^{m-1} + \ldots + a_{m-1} * 1$,
从而可以求得$a_{m-1}$,循环下去即可。
换个角度理解， 相当于给你一个数字，你怎么求得它的十进制每一位数字是什么？

**方法一**
但是这样写26进制的话不是从0开始的，所以改为A对应0，Z对应25，在相应的地方应该加减1恢复原状.

**方法二**
如果加减一不好理解，也可以用直接对应的方法，但是最终A其实是Z,B其实是A,C其实是B...以此类推。
这里注意在实际上是Z，也就是0的情况比较特殊，它不是真的0，而是一个26构成的，要减去这个26。

**方法三**
最后奉上一个递归解法

### 代码

```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        # 10进制 转换为 26进制，A对应1，B对应2,....Z对应26
        while columnNumber > 0:
            # 最右边位为取模运算的结果
            columnNumber -= 1
            # A的ASC码 65
            ans.append(chr(columnNumber%26 + 65))
            columnNumber //= 26
        return ''.join(ans[::-1])
```
```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            curr = columnNumber%26
            # 余数为1对应了A
            ans.append(chr(curr+64) if curr > 0 else 'Z')
            # 如果发生了整除的情况，我们实际上欠了一个26
            columnNumber //= 26
            if not curr:
                columnNumber -= 1
        return ''.join(ans[::-1])
```
```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return self.convertToTitle((columnNumber-1)//26) + chr((columnNumber-1)%26 + 65) if columnNumber > 0 else ''
```