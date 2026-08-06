# [Python] 在有序集合中查是否有两数和

> slug: python-zai-you-xu-ji-he-zhong-cha-shi-fo-1lva
> date: 2021-08-22
> tags: Python, Python3
> question: Two Sum III - Data structure design (two-sum-iii-data-structure-design)
> url: https://leetcode.cn/problems/two-sum-iii-data-structure-design/solutions/BI8k9i/python-zai-you-xu-ji-he-zhong-cha-shi-fo-1lva/

---
```python3
from sortedcontainers import SortedList
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = SortedList([])


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.add(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.nums) < 2:
            return False
        min_val, max_val = self.nums[0] + self.nums[1], self.nums[-1] + self.nums[-2]
        if value < min_val or value > max_val:
            return False
        l, r = 0, len(self.nums) - 1
        while l < r:
            if self.nums[l] + self.nums[r] == value:
                return True
            elif self.nums[l] + self.nums[r] < value:
                l += 1
            else:
                r -= 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
```