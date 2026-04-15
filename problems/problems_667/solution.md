# [Python/Java/TypeScript/Go] 构造题

> Author: Benhao
> Date: 2022-09-07
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
注意到题目没有说不存在构造的情况的返回，估计是全部存在构造，那构造方式一定是围绕着k的。
想到用k或k+1个数构造k-1个不同的差，剩下的数以同样的差排列
尝试构造k-1个差分别为k到2,剩下的数字差为1
发现[1-(k + 1)]以 1 (k + 1) 2 k 3 (k - 1) 这样摆动刚好构造k, k-1, k - 2, k - 3 ... 这些差, 剩下的数排列为差为1的递增数列   【注意最后一个数 k // 2 + 1 和下一个数 k + 2 的差也被摆动包含】

### 代码

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