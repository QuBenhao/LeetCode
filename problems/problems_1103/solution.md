# [Python/Go/Java/Cpp] Summation formula + inequality derivation

> Author: Benhao
> Date: 2024-06-02
> Upvotes: 2
> Tags: C++, Go, Java, Python3

---


> Problem: [1103. 分糖果 II](https://leetcode.cn/problems/distribute-candies-to-people/description/)

[TOC]

# Intuition

> Find how many full distributions are possible (the final term in the summation formula) and how many candies remain afterward (the remainder).
Once we know the number of distributions, division and remainder tell us how many rounds were completed and who received candies in the final round.

# Approach

> Use the summation formula and inequalities to estimate the number of distributions, then refine the estimate.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        x * (x + 1) // 2 >= candies > x * (x - 1) // 2
        (x + 1) * (x + 1) > x * (x + 1) >= 2 * candies > x * (x - 1) > (x - 1) * (x - 1)
        x + 1 > sqrt(2 * candies) > x - 1
        {} + 1 > x > {} - 1
        """
        f = (candies * 2) ** 0.5
        # Refine the estimate downward from the upper bound
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
