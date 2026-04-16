# [Python] 哈希表

> Author: Benhao
> Date: 2024-03-31
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/description/)


# Code
```Python3 []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            group["".join(sorted(word))].append(word)
        return [v for v in group.values()]
```
  
