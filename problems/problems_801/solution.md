# [Python/Java/TypeScript/Go] Dynamic programming

> Author: Benhao
> Date: 2022-10-10
> Upvotes: 8
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Consider swapping or keeping each adjacent pair of positions, then return the minimum

### Code

```Python3 []
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # dp0: no swap at the previous position; dp1: swapped at the previous position
        dp0, dp1 = 0, 1
        for (n10, n20), (n11, n21) in pairwise(zip(nums1, nums2)):
            tmp0, tmp1, dp0, dp1 = dp0, dp1, inf, inf
            # Can keep the current order
            if n11 > n10 and n21 > n20:
                # Neither position is swapped, or both the previous and current positions are swapped
                dp0, dp1 = tmp0, tmp1 + 1
            # Can swap
            if n11 > n20 and n21 > n10:
                # The previous position is swapped and the current one is not, or vice versa
                dp0, dp1 = min(dp0, tmp1), min(dp1, tmp0 + 1)
        return min(dp0, dp1)
```
```Java []
class Solution {
    public int minSwap(int[] nums1, int[] nums2) {
        int dp0 = 0, dp1 = 1;
        for (int i = 1, tmp0, tmp1; i < nums1.length; i++) {
            tmp0 = dp0; tmp1 = dp1; dp0 = Integer.MAX_VALUE; dp1 = Integer.MAX_VALUE;
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                dp0 = tmp0;
                dp1 = tmp1 + 1;
            }
            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                dp0 = Math.min(dp0, tmp1);
                dp1 = Math.min(dp1, tmp0 + 1);
            }
        }
        return Math.min(dp0, dp1);
    }
}
```
```TypeScript []
function minSwap(nums1: number[], nums2: number[]): number {
    let dp0: number = 0, dp1: number = 1
    for (let i = 1; i < nums1.length; i++) {
        const tmp0: number = dp0, tmp1: number = dp1
        dp0 = dp1 = Number.MAX_SAFE_INTEGER
        if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
            dp0 = tmp0
            dp1 = tmp1 + 1
        }
        if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
            dp0 = Math.min(dp0, tmp1)
            dp1 = Math.min(dp1, tmp0 + 1)
        }
    }
    return Math.min(dp0, dp1)
};
```
```Go []
func minSwap(nums1 []int, nums2 []int) int {
    dp0, dp1 := 0, 1
    for i, n := 1, len(nums1); i < n; i++ {
        tmp0, tmp1 := dp0, dp1
        dp0, dp1 = n, n
        if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1] {
            dp0, dp1 = tmp0, tmp1 + 1
        }
        if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1] {
            dp0, dp1 = min(dp0, tmp1), min(dp1, tmp0 + 1)
        }
    }
    return min(dp0, dp1)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
