# [Python/Java/TypeScript/Go] Greedy

> Author: Benhao
> Date: 2022-07-22
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
[叶总](https://leetcode.cn/problems/set-intersection-size-at-least-two/solution/by-ac_oier-3xn6/) has already explained this clearly and in detail; here I share the code and comments.

### Code

```Python3 []
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort right endpoints in ascending order to make greedy endpoint selection valid; break ties with the shortest interval, which has the fewest choices and whose selected points also cover the other intervals
        intervals.sort(key=lambda x:(x[1], -x[0]))
        # Since elements are added in increasing order, the two largest elements suffice to decide whether to add more
        a, b, ans = -1, -1, 0
        for left, right in intervals:
            # If the left endpoint is beyond the current largest element, add two new points from this interval (view this recursively: earlier points no longer matter)
            if left > b:
                # Greedily take the two largest points
                a, b, ans = right - 1, right, ans + 2
            # If the left endpoint lies between the two largest elements, the largest element is already a point in this interval
            elif left > a:
                # We need one more point; greedily take this interval's largest point, making the old b the second largest
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
