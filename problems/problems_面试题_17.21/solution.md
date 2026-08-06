# [Python] 栈（想象成每次我们都把前面的缝隙填满了）和双指针（我们总有左边最大和右边最大）

> slug: python-zhan-xiang-xiang-cheng-mei-ci-wo-gt54l
> date: 2021-04-02
> tags: Python
> question: Volume of Histogram LCCI (volume-of-histogram-lcci)
> url: https://leetcode.cn/problems/volume-of-histogram-lcci/solutions/IHdQRc/python-zhan-xiang-xiang-cheng-mei-ci-wo-gt54l/

---
### 解题思路
**栈的思路**
我们计算存水的时候，不在乎前面最大的高度往前的高度，也就是我们每次清栈都是栈中比当前小的元素。
我们计算两个柱子间的存水要根据较矮的一侧。
考虑 [5,0,3,0,2,0,5]的情况：
- 到3的时候，栈中是[5,0]，我们发现可以存水了，0出来是低处的高度，能存(3-0) * (2-0-1) = 3 的水；（可以注意到3上面的部分后面的5也能存，但他们还在栈中所以还能计算）
- 到2的时候，栈中是[5,3,0], 又可以存水了，0是低处，现在想象成前面已经是[5,3,3,0,2]了，能存(2-0)*(4-2-1)=2的水；（这个时候可以理解为前面变为[5,3,3,2,2]了）
- 最后到5的时候，栈中是[5,3,2,0],分别依次计算对应能存的水量，
- 5和2之间能存(2-0)*(6-4-1)=2; 计算后相当于变成了[5,3,3,2,2,2,5]
- 5和3之间能存(3-2)*(6-2-1)=3; 这里因为上一个2之间已经被填满了,计算后相当于变成[5,3,3,3,3,3,5]
- 最后，5和5之间能存(5-3)*(6-0-1)=10;
所以答案就是以上计算累加。

**双指针思路**
考虑我们每次计算每个格子可能存的水，那么就需要根据它的左右两边的最高值。
指针的移动是尽可能想超过另一侧的高度来移动的。
先证明: 
当`height[left] <= height[right]`的时候，`left_max <= height[right]`
当`height[right] < height[left]`的时候，`right_max < height[left]`
采取反证法:
如果height[left] <= height[right] < left_max，
那么存在left左边比当前right大的值比如说height[left']，当left=left',right所在的值使得left向右移动了，也就是存在一个right右边的值，height[right']>=height[left'].
那么是怎么存在一个left的值，让这个right左移了呢？
显然不存在的，因为left_max <= height[right']。
证毕。

也就是说，left不是最大值的时候，也就是height[left] <= left_max <= height[right],显然left处可以存left_max-height[left]这么多水。
反之亦然。

### 代码

栈
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

双指针
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