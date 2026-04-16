# [Python/Go/Java/Cpp] 数学求和公式+不等式推算

> Author: Benhao
> Date: 2024-06-02
> Upvotes: 2
> Tags: C++, Go, Java, Python3

---


> Problem: [1103. 分糖果 II](https://leetcode.cn/problems/distribute-candies-to-people/description/)

[TOC]

# 思路

> 我们能发多少次(求和公式的末项), 我们发完剩下的发不出去的是多少个 (余数)
假设我们知道发了多少次，那么我们就知道发了多少轮，最后一轮发到了谁 (除余)

# 解题方法

> 通过求和公式，不等式，推算大致发了多少次，再计算逼近

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        x * (x + 1) // 2 >= candies > x * (x - 1) // 2
        (x + 1) * (x + 1) > x * (x + 1) >= 2 * candies > x * (x - 1) > (x - 1) * (x - 1)
        x + 1 > 根号下(2 * candies) > x - 1
        {} + 1 > x > {} - 1
        """
        f = (candies * 2) ** 0.5
        # 从最大往最小逼近
        x = int(f + 1)
        if (s := x * (x + 1) // 2) > candies:
            s -= x
            if s > candies:
                x -= 1
                s -= x
            x -= 1
        remain = candies - s
        d, m = divmod(x, num_people)
        ans = [0] * num_people
        for i in range(num_people):
            ans[i] = (i + 1) * d + num_people * (d - 1) * d // 2
            if i < m:
                ans[i] += i + 1 + num_people * d
        ans[m] += remain
        return ans
```
```Golang []
func distributeCandies(candies int, num_people int) []int {
	// (x + 2)^2 > (x + 2) * (x + 1) > 2 * candies >= x * (x + 1) > x^2
	f := math.Sqrt(float64(candies * 2))
	x := int(f + 1)
	var s int
	for s = x * (x + 1) / 2; s > candies; x-- {
		s -= x
	}
	remain := candies - s
	div, mod := x/num_people, x%num_people
	ans := make([]int, num_people)
	for i := 0; i < num_people; i++ {
		ans[i] += (i+1)*div + num_people*div*(div-1)/2
		if i < mod {
			ans[i] += num_people*div + i + 1
		}
	}
	ans[mod] += remain
	return ans
}
```
```Java []
class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        double f = Math.sqrt(candies * 2);
        int x = (int)f + 1, s;
        for (s = x * (x + 1) / 2; s > candies; x--) {
            s -= x;
        }
        int remain = candies - s, div = x / num_people, mod = x % num_people;
        int[] ans = new int[num_people];
        for (int i = 0; i < num_people; i++) {
            ans[i] = (i + 1) * div + num_people * div * (div - 1) / 2;
            if (i < mod) {
                ans[i] += num_people * div + i + 1;
            }
        }
        ans[mod] += remain;
        return ans;
    }
}
```
```Cpp []
class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        double f = sqrt(candies * 2);
        int x = (int)(f + 1), s;
        for (s = x * (x + 1) / 2; s > candies; x--) {
            s -= x;
        }
        int remain = candies - s, d = x / num_people, m = x % num_people;
        vector<int> ans;
        for (int i = 0; i < num_people; i++) {
            ans.push_back((i + 1) * d + num_people * d * (d - 1) / 2);
            if (i < m) {
                ans[ans.size() - 1] += num_people * d + i + 1;
            }
        }
        ans[m] += remain;
        return ans;
    }
};
```