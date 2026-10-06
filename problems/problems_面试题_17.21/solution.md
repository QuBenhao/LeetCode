# [Python] Stack (imagine filling earlier gaps at each step) and two pointers (track the maximum heights on both sides)

> slug: python-zhan-xiang-xiang-cheng-mei-ci-wo-gt54l
> date: 2021-04-02
> tags: Python
> question: Volume of Histogram LCCI (volume-of-histogram-lcci)
> url: https://leetcode.cn/problems/volume-of-histogram-lcci/solutions/IHdQRc/python-zhan-xiang-xiang-cheng-mei-ci-wo-gt54l/

---
### Approach
**Stack approach**
When calculating trapped water, heights before the highest preceding bar no longer matter. Each stack-clearing step therefore removes entries lower than the current bar.
The water trapped between two bars is bounded by the shorter side.
Consider [5,0,3,0,2,0,5]:
- At 3, the stack is [5,0], and water can be trapped. Pop 0 as the bottom height, giving (3-0) * (2-0-1) = 3 units of water. (The later 5 can also trap water above 3, but those bars remain in the stack for later calculation.)
- At 2, the stack is [5,3,0], so more water can be trapped. The bottom height is 0; imagine the prefix is already [5,3,3,0,2]. This traps (2-0)*(4-2-1)=2 units of water. (The prefix can now be viewed as [5,3,3,2,2].)
- At the final 5, the stack is [5,3,2,0]. Calculate the trapped water for each level in turn:
- Between 5 and 2, trap (2-0)*(6-4-1)=2; after this calculation, the array is effectively [5,3,3,2,2,2,5].
- Between 5 and 3, trap (3-2)*(6-2-1)=3. The gap up to height 2 has already been filled, so the array is now effectively [5,3,3,3,3,3,5].
- Finally, between 5 and 5, trap (5-3)*(6-0-1)=10;
add these amounts to obtain the answer.

**Two-pointer approach**
To calculate the water above each position, use the maximum heights to its left and right.
Move the pointer on the shorter side, seeking a height that can exceed the opposite side.
First, prove: 
when `height[left] <= height[right]`, `left_max <= height[right]`;
when `height[right] < height[left]`, `right_max < height[left]`.
Proof by contradiction:
Suppose height[left] <= height[right] < left_max.
Then there is a height to the left of left, say height[left'], greater than the current height[right]. When left=left', the right-side height allowed left to move right, so there must be a position right' to the right of right with height[right']>=height[left'].
But what value on the left could then have allowed right to move left?
No such value exists, because left_max <= height[right'].
This completes the proof.

Thus, when left is not the maximum, height[left] <= left_max <= height[right], and position left can hold left_max-height[left] units of water.
The symmetric argument applies to the other side.

### Code

Stack
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack, ans = [], 0
        for i,v in enumerate(height):
            while stack and height[stack[-1]] < v:
                # height between left upper and right upper
                h = height[stack.pop()]
                if not stack:
                    break
                # since the area of lower area has been computed, minus the height
                ans += (min(height[stack[-1]], height[i]) - h) * (i - stack[-1] - 1)
            stack.append(i)
        return ans

```

Two pointers
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n, ans = len(height), 0
        left, right, left_max, right_max = 0, n - 1, 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    # height[left] <= left_max <= height[right]
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
```
