# [Python] For duplicates, extend only the subsets affected by the previous occurrence

> Author: Benhao
> Date: 2021-03-31
> Upvotes: 1
> Tags: Python

---

### Approach
The first idea was bfs, using a set to filter duplicate results, but this introduces many unnecessary repeated choices. (First code block.)
After sorting, indices can be used to determine whether elements are equal and whether the previous equal element is already in a subset. (Second code block.)
The key to the second approach is the number of subsets affected by the previous equal element, so we only need to record that count. (Third code block.)

### Code
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

We only want to append a duplicate element to subsets that contain its previous occurrence.
For example, [1,2,2]
We already have [[1],[1,2],[2]]. The final 2 should only be appended to subsets containing the previous 2. Adding it to subsets without 2 would duplicate the results of adding the previous occurrence.
The result is therefore [[1],[1,2],[2],[1,2,2],[2,2]].
ans actually includes the empty subset [], but zip cannot provide its first element, so skip it and add it separately.

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

For equal elements, record the number of subsets affected by the previous occurrence and extend only those that received that element.
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
