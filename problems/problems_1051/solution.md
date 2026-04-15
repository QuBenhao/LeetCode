# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-06-12
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
直接排序比较或根据题目范围计数比较

### 代码

```Python3 []
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))
```
```Java []
class Solution {
    public int heightChecker(int[] heights) {
        int n = heights.length, ans = 0;
        int[] sorted = Arrays.copyOf(heights, n);
        Arrays.sort(sorted);
        for (int i = 0; i < n; i++) {
            if (sorted[i] != heights[i]) {
                ans++;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function heightChecker(heights: number[]): number {
    const n = heights.length
    const arr = new Array()
    for (const h of heights) {
        arr.push(h)
    }
    arr.sort((a, b) => a - b)
    let ans = 0
    for (let i = 0; i < n; i++) {
        if (arr[i] != heights[i]) {
            ans++
        }
    }
    return ans
};
```
```Go []
func heightChecker(heights []int) (ans int) {
    n := len(heights)
    arr := make([]int, n)
    copy(arr, heights)
    sort.Ints(arr)
    for i := 0; i < n; i++ {
        if arr[i] != heights[i] {
            ans++
        }
    }
    return
}
```
计数
```Python3 []
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnts, mx, ans, idx = Counter(heights), max(heights), 0, 0
        for i in range(1, mx + 1):
            for _ in range(cnts[i]):
                ans += heights[idx] != i
                idx += 1
        return ans
```
```Java []
class Solution {
    public int heightChecker(int[] heights) {
        Map<Integer, Integer> counter = new HashMap<>();
        int max = 0;
        for (int h: heights) {
            counter.put(h, counter.getOrDefault(h, 0) + 1);
            max = Math.max(max, h);
        }
        int ans = 0, idx = 0;
        for (int i = 1; i <= max; i++) {
            for (int j = 0; j < counter.getOrDefault(i, 0); j++) {
                if (heights[idx++] != i) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
```
```TypeScript []
function heightChecker(heights: number[]): number {
    const counter = new Map()
    let max = 0, ans = 0, idx = 0
    for (const h of heights) {
        if (counter.has(h)) {
            counter.set(h, counter.get(h) + 1)
        } else {
            counter.set(h, 1)
        }
        max = Math.max(max, h)
    }
    for (let i = 1; i <= max; i++) {
        if (counter.has(i)) {
            for (let j = 0; j < counter.get(i); j++) {
                if (heights[idx++] != i) {
                    ans++
                }
            }
        }
    }
    return ans
};
```
```Go []
func heightChecker(heights []int) (ans int) {
    counter, mx, idx := map[int]int{}, 0, 0
    for _, h := range heights {
        counter[h]++
        mx = max(mx, h)
    }
    for i := 1; i <= mx; i++ {
        for j := 0; j < counter[i]; j++ {
            if heights[idx] != i {
                ans++
            }
            idx++
        }
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```