# [Python/Go/Java/Cpp] 模拟

> Author: Benhao
> Date: 2024-06-02
> Upvotes: 1
> Tags: C++, Go, Java, Python3

---


> Problem: [1523. 在区间范围内统计奇数数目](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/description/)

[TOC]

# 思路

> 每两个数里就有一个数是奇数，high到low之间一共有(high - low) // 2组成对。再额外加上某一端是奇数即可

# 解题方法

> 比如3-7: 3,4; 5,6; 为两组；7为额外奇数
再比如6-9: 6,7为一组; 9为额外奇数

# 复杂度

时间复杂度:
> $O(1)$

空间复杂度:
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