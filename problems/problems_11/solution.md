# [Python/Golang/Java/Cpp] Two pointers 

> Author: Benhao
> Date: 2024-03-05
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/description/)

[TOC]

# Intuition

> Two pointers

# Approach

> With pointers left and right, the shorter side determines the height, so the other endpoint is already the farthest possible choice for that shorter side. For example, when `height[left] < height[right]`, moving left to the right rules out pairing left with any index in `[left+1,right-1]`, because all of those areas must be smaller than the area of (left, right).
Moving the pointers this way repeatedly rules out many candidates that do not need to be calculated.


# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, ans = 0, len(height) - 1, -inf
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
```
```Golang []
func maxArea(height []int) (ans int) {
	for i, j := 0, len(height)-1; i < j; {
		ans = max(ans, min(height[i], height[j])*(j-i))
		if height[i] > height[j] {
			j--
		} else {
			i++
		}
	}
	return
}
```
```Java []
class Solution {
    public int maxArea(int[] height) {
        int ans = 0;
        for (int i = 0, j = height.length - 1; i < j; ) {
            ans = Math.max(ans, Math.min(height[i], height[j]) * (j - i));
            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }
        return ans;
    }
}
```
```C++ []
class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0;
        for (int i = 0, j = height.size() - 1; i < j; ) {
            ans = max(ans, min(height[i], height[j]) * (j - i));
            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }
        return ans;
    }
};
```
  
