# [Python/Go/Java/Cpp] Simulation

> Author: Benhao
> Date: 2024-06-02
> Upvotes: 1
> Tags: C++, Go, Java, Python3

---


> Problem: [1523. 在区间范围内统计奇数数目](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/description/)

[TOC]

# Intuition

> Each pair of consecutive numbers contains one odd number. There are (high - low) // 2 pairs between low and high; add one more if either endpoint is odd.

# Approach

> For example, 3-7 has two pairs, 3,4 and 5,6, with 7 as the extra odd number.
For 6-9, 6,7 is one pair, with 9 as the extra odd number.

# Complexity

Time complexity:
> $O(1)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 == 1 or high % 2 == 1)
```
```Golang []
func countOdds(low int, high int) (ans int) {
	ans = (high - low) / 2
	if low&1 == 1 || high&1 == 1 {
		ans++
	}
	return
}
```
```Java []
class Solution {
    public int countOdds(int low, int high) {
        return ((high - low) >> 1) + (((low & 1) == 1 || (high & 1) == 1) ? 1 : 0);
    }
}
```
```Cpp []
class Solution {
public:
    int countOdds(int low, int high) {
        return (high - low) / 2 + ((low & 1) == 1 || (high & 1) == 1);
    }
};
```
