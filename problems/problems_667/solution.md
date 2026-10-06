# [Python/Java/TypeScript/Go] Constructive solution

> Author: Benhao
> Date: 2022-09-07
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
The problem does not specify what to return when construction is impossible, so a construction presumably always exists. It must be organized around k.
Try using k or k+1 numbers to construct k-1 distinct differences, with all remaining numbers sharing the same difference.
Construct k-1 differences from k down to 2, then use a difference of 1 for the remaining numbers.
Alternating the values in [1-(k + 1)] as 1 (k + 1) 2 k 3 (k - 1) produces differences k, k-1, k - 2, k - 3 ... . Arrange the remaining values in ascending order with a difference of 1. [Note: the difference between the last alternating value, k // 2 + 1, and the next value, k + 2, has already appeared in the alternating part.]

### Code

```Python3 []
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []
        for i in range(1, (k + 1) // 2 + 1):
            ans.append(i)
            ans.append(k + 2 - i)
        if k % 2 == 0:
            ans.append(1 + k // 2)
        return ans + [i for i in range(k + 2, n + 1)]
```
```Java []
class Solution {
    public int[] constructArray(int n, int k) {
        int[] ans = new int[n];
        int idx = 0;
        for (int i = 1; i <= (k + 1) / 2; i++) {
            ans[idx++] = i;
            ans[idx++] = k + 2 - i;
        }
        if (k % 2 == 0) {
            ans[idx++] = k / 2 + 1;
        }
        for (int i = k + 2; i <= n; i++) {
            ans[idx++] = i;
        }
        return ans;
    }
}
```
```TypeScript []
function constructArray(n: number, k: number): number[] {
    const ans: Array<number> = new Array<number>(n).fill(0)
    let idx: number = 0
    for (let i = 1; i <= (k + 1) >> 1; i++) {
        ans[idx++] = i
        ans[idx++] = k + 2 - i
    }
    if (k % 2 == 0) {
        ans[idx++] = (k >> 1) + 1
    }
    for (let i = k + 2; i <= n; i++) {
        ans[idx++] = i
    }
    return ans
};
```
```Go []
func constructArray(n int, k int) []int {
    ans := make([]int, n)
    idx := 0
    for i := 1; i <= (k + 1) / 2; i++ {
        ans[idx] = i
        ans[idx + 1] = k + 2 - i
        idx += 2
    }
    if k % 2 == 0 {
        ans[idx] = k / 2 + 1
        idx++
    }
    for ; idx < n; idx++ {
        ans[idx] = idx + 1
    }
    return ans
}
```
