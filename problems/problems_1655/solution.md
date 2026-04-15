# [Python] 贪心记忆化搜索

> Author: Benhao
> Date: 2021-06-10
> Upvotes: 0
> Tags: Python, Python3

---

### 解题思路
统计数的频次，将频次从大到小排序，取前`len(quantity)`个!（如果连前面数组长度的频次都无法满足，加上后面的就更不可能了）
使用tuple记录当前的可选频次,每次遍历合理分配即可。

### 代码

```python3
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = Counter(nums)
        m = len(quantity)
        options = [val for val in c.values()]
        options.sort(reverse=True)

        @lru_cache(None)
        def dfs(idx, ops):
            if idx == m:
                return True
            if ops[0] < quantity[idx]:
                return False
            
            for i in range(len(ops)):
                if ops[i] < quantity[idx]:
                    break
                temp = list(ops)
                temp[i] -= quantity[idx]
                temp.sort(reverse=True)
                if dfs(idx+1, tuple(temp)):
                    return True
            return False
        
        return dfs(0, tuple(options[:m]))
```