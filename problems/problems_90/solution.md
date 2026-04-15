# [Python] 相同的时候只需要添加上一个影响的长度

> Author: Benhao
> Date: 2021-03-31
> Upvotes: 1
> Tags: Python

---

### 解题思路
首先想到bfs，根据set的特性来筛除相同的结果，但是显然这样增加了很多不必要的重复选择。（第一段代码）
而排序后，下标就可以用来判断是否相同，相同的那个元素是否在列表中等判断了。（第二段代码）
根据第二个的思路，其实核心就是上一个相同元素影响的长度，那我们只需要记一下长度即可（第三段代码）

### 代码
```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n, subsets = len(nums), set()

        def bfs(index, curr_list):
            if index == n:
                subsets.add(tuple(curr_list))
                return
            bfs(index+1, curr_list)
            bfs(index+1, curr_list+[nums[index]])

        bfs(0, [])
        return [list(x) for x in subsets]

```

我们只想把相同的元素添加在所有有前一个元素的列表中。
比如说[1,2,2]
我们前面有[[1],[1,2],[2]]，这个时候最后一个2只想添加在有前一个2中的，而没有2的再添加就会造成和添加前一个的重复了。
所以是[[1],[1,2],[2],[1,2,2],[2,2]]。
其实ans里是有[]空集的，但是空集没法zip后取第一个元素，所以就跳过它再单独添加了。

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = [[]]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                ans += [x+[(nums[i],i)] for x in ans if x and x[-1][1] == i-1]
            else:
                ans += [x+[(nums[i],i)] for x in ans]
        return [[]] + [list(list(zip(*x))[0]) for x in ans if x]
```

统计一下相同的时候上一个影响的长度，只对添加了相同元素的进行添加
```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = [[]]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                ans += [x+[nums[i]] for x in ans[len(ans) - last:]]
            else:
                last = len(ans)
                ans += [x+[nums[i]] for x in ans]
        return ans
```