# [Python/C] 反着看交换的顺序其实就很清晰了

> Author: Benhao
> Date: 2021-03-28
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---

### 解题思路
如果两倍在n以内，就到两倍的位置，否则就到乘2-n+1（奇数）位置。

### 代码

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