# [Python/Golang/Java/Cpp] 双指针 

> Author: Benhao
> Date: 2024-03-05
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/description/)

[TOC]

# 思路

> 双指针

# 解题方法

> 左右指针left和right,计算高度会以短板计算，所以对短板来说另一头已经是最远的选择了。比如`height[left] < height[right]`，我们将left指针右移，实际上是否定了所有区间`[left+1,right-1]`和left的组合区域面积，因为它们必然小于(left, right)的面积。
以这样的思路移动指针可以不停地否定诸多不必要计算的答案。


# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
