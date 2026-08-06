# [Python/Java/TypeScript/Go] 二分

> slug: pythonjavatypescriptgo-er-fen-by-himymbe-wzyt
> date: 2022-06-06
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Koko Eating Bananas (koko-eating-bananas)
> url: https://leetcode.cn/problems/koko-eating-bananas/solutions/GKTp5S/pythonjavatypescriptgo-er-fen-by-himymbe-wzyt/

---
### 解题思路
标准的搭配helper函数的二分应用题 (Py中为lambda函数)

### 代码

```Python3 []
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(1, max(piles) + 1), True, key=lambda x: sum(ceil(p / x) for p in piles) <= h) + 1
```
```Java []
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1, right = max(piles);
        while(left < right) {
            int mid = left + right >> 1;
            if (helper(mid, piles, h)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean helper(int x, int[] piles, int h) {
        int s = 0;
        for(int p: piles) {
            s += p % x == 0 ? p / x : p / x + 1;
        }
        return s <= h;
    }

    private int max(int[] nums) {
        int m = 0;
        for(int num: nums) {
            m = Math.max(m, num);
        }
        return m;
    }
}
```
```TypeScript []
function minEatingSpeed(piles: number[], h: number): number {
    let left = 1, right = Math.max(...piles)
    const helper = (x: number): boolean => {
        let s = 0
        for(const p of piles) {
            s += Math.ceil(p / x)
        }
        return s <= h
    }
    while (left < right) {
        const mid = (left + right) >> 1
        if (helper(mid)) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
};
```
```Go []
func minEatingSpeed(piles []int, h int) int {
    left, right := 1, max(piles)
    helper := func(x int) bool {
        s := 0
        for _, p := range piles {
            s += (p + x - 1) / x
        }
        return s <= h
    }
    for left < right {
        mid := (left + right) >> 1
        if helper(mid) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

func max(nums []int) int {
    ans := nums[0]
    for _, num := range nums {
        if num > ans {
            ans = num
        }
    }
    return ans
}
```