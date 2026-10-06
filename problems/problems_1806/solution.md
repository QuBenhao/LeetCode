# [Python/C] The permutation order is clearer when viewed in reverse

> Author: Benhao
> Date: 2021-03-28
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---

### Approach
If doubling the index stays below n, move to twice the index; otherwise, move to 2 * index - n + 1, an odd position.

### Code

```Python3 []
class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        mid = n // 2
        track = 1
        while track != mid:
            if track * 2 < n:
                track *= 2
            else:
                track = track * 2 + 1 - n
            ans += 1
        return ans
```
```C []
int reinitializePermutation(int n){
    int ans = 1, mid = n / 2, track = 1;
    while (track != mid) {
        if (track * 2 < n) {
            track *= 2;
        } else {
            track = track * 2 + 1 - n;
        }
        ans++;
    }
    return ans;
}
```
