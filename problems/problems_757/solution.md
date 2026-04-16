# [Python/Java/TypeScript/Go] 贪心

> Author: Benhao
> Date: 2022-07-22
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
[叶总](https://leetcode.cn/problems/set-intersection-size-at-least-two/solution/by-ac_oier-3xn6/)讲的很好很详细了，这里分享一下代码和注释。

### 代码

```Python3 []
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 右端点从小到大，保证贪心处理边缘点的正确性，同时右端点一样的时候优先处理长度最短的区间，因为该区间可选点最少同时会覆盖其他区间
        intervals.sort(key=lambda x:(x[1], -x[0]))
        # 由于我们是单调递增添加元素，维护当前集合前二大的元素即可判断是否需要添加新的
        a, b, ans = -1, -1, 0
        for left, right in intervals:
            # 如果区间左端点也在当前最大元素的右边，说明需要从该区间添加两个新点(可以理解为递归，前面的不再起作用)
            if left > b:
                # 贪心取最大的两个点
                a, b, ans = right - 1, right, ans + 2
            # 如果区间左端点位于当前最大元素与次大元素的中间，说明最大元素本身是区间内的一个点了
            elif left > a:
                # 我们还需要再取一个，贪心取该区间最大，原来的b成为次大
                a, b, ans = b, right, ans + 1
        return ans
```
```Java []
class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[1] != b[1]) {
                return a[1] - b[1];
            }
            return b[0] - a[0];
        });
        int a = -1, b = -1, ans = 0;
        for (int[] i: intervals) {
            int left = i[0], right = i[1];
            if (left > b) {
                a = right - 1;
                b = right;
                ans += 2;
            } else if (left > a) {
                a = b;
                b = right;
                ans++;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function intersectionSizeTwo(intervals: number[][]): number {
    intervals.sort((a, b) => {
        if (a[1] != b[1]) {
            return a[1] - b[1]
        }
        return b[0] - a[0]
    })
    let a = -1, b = -1, ans = 0
    for (const [left, right] of intervals) {
        if (left > b) {
            a = right - 1
            b = right
            ans += 2
        } else if (left > a) {
            a = b
            b = right
            ans++
        }
    } 
    return ans
};
```
```Go []
func intersectionSizeTwo(intervals [][]int) (ans int) {
    sort.Slice(intervals, func(i, j int) bool {
        a, b := intervals[i], intervals[j]
        return a[1] < b[1] || (a[1] == b[1] && a[0] > b[0])
    })
    a, b := -1, -1
    for _, i := range intervals {
        left, right := i[0], i[1]
        if left > b {
            a, b, ans = right - 1, right, ans + 2
        } else if left > a {
            a, b, ans = b, right, ans + 1
        }
    }
    return
}
```