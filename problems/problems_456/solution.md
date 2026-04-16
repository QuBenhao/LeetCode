# [Python] 单调栈及思考过程

> Author: Benhao
> Date: 2021-03-24
> Upvotes: 2
> Tags: Python

---

### 解题思路
题目是找三个数字，左边最小，中间最大，那么一共有六种找法：
- 先找1，3，最后找2
- 先找1，2，最后找3
- 先找3，2，最后找1
- 先找3，1，最后找2
- 先找2，3，最后找1
- 先找2，1，最后找3

不难看出第一种找法很难，因为我们需要检查2的上下界。
如果这里是先找1，2，再找3的话，相对就会简单了一些。我们省去了检查3和1的大小比对。
所以第二种、第三种、第五种、第六种更简单。

我们倾向于一个方向来找答案。
如果先找1，2，再找3，我们需要从左边找1、从右边找2，这其实很困难。

而第五种先找2，3，最后找1，是从右往左的单方向的最简单的方式了。
使用一个单调栈来维护目前的值的大小顺序，可以保证找到一个比栈中元素大的值，而栈中元素又都是在右边的元素，那么3和2就找到了。
一直pop可以保证第三个值可以尽可能的大。

### 代码

```python
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        We have a six options for solving this problem 132
        1. Get 1 3 then 2
        2. Get 1 2 then 3
        3. Get 3 2 then 1
        4. Get 3 1 then 2
        5. Get 2 3 then 1
        6. Get 2 1 then 3
        
        What is a easiest way for this problem.
        First, finding 1, 3 then 2 is difficult. 
        because we checked double for finding 2. upper and lower. 
        However, Get 1, 2 then 3 is easy. we check only one for finding 3. we do not have to check 3 with 1.
        So Method 2, 3, 5, 6 is good.
        
        And I want to check numbers only one direction.
        If I select 1, 2 then 3, I need to select 1 from left direction and select 2 from right direction.
        It is difficult.
        
        If I select numbers from left, That is Method 1. If I select numbers from right, that is Method 5.
        
        So Method 5 is easiest way for this problem.
        Left Problem is how to write the code for method 5.
        
        The 3 is always the maximum from right. It is clear.
        The 2 is a maximum number which in 3's left. => This part is O(N)
        But If we use stack, we can optimize this part to O(1)
        """
        last, stack = float("-inf"), []
        for num in reversed(nums):
            if num < last:
                return True
            while stack and stack[-1] < num:
                last = stack.pop()
            stack.append(num)
        return False

```