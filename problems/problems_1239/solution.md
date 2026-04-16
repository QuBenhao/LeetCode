# [Python] 直白朴素的01背包 到 回溯(两个剪枝加速)

> Author: Benhao
> Date: 2021-06-18
> Upvotes: 23
> Tags: Python, Python3

---

### 解题思路
一个字符串可以作为答案当且仅当其中没有重复的字符(包括我们在拼接字符串以后,拼接的字符串也同理)
所以维护一个之前所有的合法的拼接字符串,判断当前所有能组成的合理的字符串，最后返回最大值即可。
<br>
上面的方法有一个问题就是**需要维护从头到尾全部的拼接字符串**,而使用回溯法解决01背包问题恰好可以避免做这件事 。
考虑到达idx位置时，我们已知当前拼接的字符串（idx前面的01背包选择），我们要搜索后面的所有选择的可能性组成的所有结果，但是每次考虑完某种加入某个东西的背包后，我们后面需要回退回不加它的背包，再重新尝试后面的结果。这个结果搜索完后，我们才会回退到前面的01背包的选择，去回溯产生新的背包。
换句话说,当前分枝上的两个子分支，一个是加入i的(递归调用的dfs(i+1))，一个是不加i的(i后面的循环)
<br>
**回溯使用了两个剪枝**
一个是`初始预估的最大的答案，搜索找到最大答案了自然可以直接返回`。
另一个是对当前背包和当前最大值的一个评估，`如果当前的背包加上启发式预估后面的最大结果(这里面可以和当前背包重复)都无法超过当前的答案，没有搜索的必要了`。(也可以使用`len(set(self.curr).union(*arr[idx:]))`来作为不能和当前背包重复的启发式结果，测试了一下感觉性能、剪枝效果不如用可以重复的)
<br>
- Python回溯代码中可能存在的不能理解的点:
    - 新的arr由合理的字符串的集合们组成
    - 启发式预估是忽略了背包选择的限制条件的(不管有没有用到里面的字符，随便加入)
    - 使用集合可以快速判断交集是否为空
    - 集合A,B: A.union(B) = A | B = $A \cup B$
    - 集合A,B: A & B = $A \cap B$, A & B is None $\iff A \cap B = \emptyset$
    - 集合A,B: A ^ B = $(A \cup B) \setminus (A \cap B)$, 由于题目中交集为B,所以也可以使用self.curr -= arr[i]代替回溯方法

### 代码

```python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def validStr(string):
            return len(set(string)) == len(string)
        
        dp = []
        for s in arr:
            if not validStr(s):
                continue
            for s_ in list(dp):
                if validStr(s_ + s):
                    dp.append(s_ + s)
            dp.append(s)
        return len(max(dp,key=len)) if dp else 0

```

```python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 预处理数据, 去掉带有重复字符的字符串
        arr = [t for s in arr if len(t:=set(s)) == len(s)]
        # 启发式预估最大的结果
        predict = len(set().union(*arr))
        n = len(arr)
        self.curr = set()
        self.ans = 0

        def dfs(idx):
            # 更新当前背包中的长度到答案
            self.ans = max(self.ans, len(self.curr))
            # 找到能拼接出最大可能结果的结果了，不需要继续搜索 或者 当前的背包加上后面最长的结果都无法超过当前的答案了，不需要继续搜索
            if self.ans == predict or idx == n or len(self.curr) + len(set().union(*arr[idx:])) < self.ans:
                return
            # 从idx到n,根据回溯寻找01背包最大值
            for i in range(idx, n):
                # 当前背包与arr[idx]不冲突
                if not self.curr & arr[i]:
                    # 加入背包, A+B
                    self.curr |= arr[i]
                    # 判断新的背包的最大值
                    dfs(i+1)
                    # 回溯继续寻找最大值, (A+B) - B
                    self.curr ^= arr[i]
        
        dfs(0)
        return self.ans
```