# [Python/Java/TypeScript/Go] 排序哈希 -> 左右最大最小值

> Author: Benhao
> Date: 2022-08-12
> Upvotes: 28
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
最终的目的既然是让整个数组有序，那么每一个分块各个数字的个数都是和排序后各个数字的计数一致的。
想要分的最多，只要一致就分出一块即可。

其实不需要排序，只要左边分块的最大值，比右边所有数的最小值都不大的话，那么这个分块就不会影响最终的排序。
我们只需要遍历统计左边最大值，右边最小值即可。(类似接雨水)

### 代码

```python3
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnts, ans = defaultdict(int), 0
        for num, sorted_num in zip(arr, sorted(arr)):
            cnts[num] += 1
            if not cnts[num]:
                del cnts[num]
            cnts[sorted_num] -= 1
            if not cnts[sorted_num]:
                del cnts[sorted_num]
            if not cnts:
                ans += 1
        return ans
```

```Python3 []
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        mx, mn = [-1] * n, [inf] * n
        for i in range(n):
            mx[i], mn[-1-i] = max(mx[i-1],arr[i]), min(mn[-i],arr[-1-i])
        # 所有的分割点i，段的个数是割点个数+1
        return sum(mx[i - 1] <= mn[i] for i in range(1, n)) + 1
```
```Java []
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int n = arr.length, ans = 0;
        int[] max = new int[n], min = new int[n];
        max[0] = arr[0];
        min[n - 1] = arr[n - 1];
        for(int i = 1; i < n; i++) {
            max[i] = Math.max(max[i - 1], arr[i]);
            min[n - 1 - i] = Math.min(min[n - i], arr[n - 1 - i]);
        }
        for (int i = 1; i < n; i++) {
            if (max[i - 1] <= min[i]) {
                ans++;
            }
        }
        // 段的个数是割点个数+1
        return ++ans;
    }
}
```
```TypeScript []
function maxChunksToSorted(arr: number[]): number {
    const n: number = arr.length
    let ans: number = 0
    const max: Array<number> = new Array<number>(n), min: Array<number> = new Array<number>(n)
    max[0] = arr[0]
    min[n - 1] = arr[n - 1]
    for (let i = 1; i < n; i++) {
        max[i] = Math.max(max[i - 1], arr[i])
        min[n - 1 - i] = Math.min(min[n - i], arr[n - 1 - i])
    }
    for (let i = 1; i < n; i++) {
        if (max[i - 1] <= min[i]) {
            ans++
        }
    }
    // 段的数量为割点数+1
    return ++ans
};
```
```Go []
func maxChunksToSorted(arr []int) (ans int) {
    n := len(arr)
    mx, mn := make([]int, n), make([]int, n)
    mx[0], mn[n - 1] = arr[0], arr[n - 1]
    for i := 1; i < n; i++ {
        mx[i] = max(mx[i - 1], arr[i])
        mn[n - 1 - i] = min(mn[n - i], arr[n - 1 - i])
    }
    for i := 1; i < n; i++ {
        if mx[i - 1] <= mn[i] {
            ans++
        }
    }
    // 段的数量为割点数+1
    ans++
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
