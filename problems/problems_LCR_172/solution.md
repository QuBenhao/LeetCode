# [Python] 标准的二分题目(100%)

> slug: python-biao-zhun-de-er-fen-ti-mu-100-by-2ossr
> date: 2021-07-15
> tags: Python, Python3
> question: 统计目标成绩的出现次数 (zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof)
> url: https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solutions/AxPXJW/python-biao-zhun-de-er-fen-ti-mu-100-by-2ossr/

---
```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect_right(nums, target) - bisect_left(nums, target)
```