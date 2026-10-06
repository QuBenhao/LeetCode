# [Python/Java/JavaScript/Go] Simulation

> Author: Benhao
> Date: 2022-02-04
> Upvotes: 9
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Take the minimum of each pair, then count how many attain the maximum of those minima.

### Code

```Python3 []
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        return nums.count(m) if (nums := [min(r) for r in rectangles]) and (m := max(nums)) else 0
```
```Java []
class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int max = 0, ans = 0;
        for(int[] r: rectangles){
            int cur = Math.min(r[0], r[1]);
            if(cur > max){
                max = cur;
                ans = 1;
            } else if(cur == max)
                ans++;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    let max = 0, ans = 0
    for(const r of rectangles) {
        const cur = Math.min(r[0], r[1])
        if(cur > max) {
            max = cur
            ans = 1
        } else if(cur == max)
            ans++
    }
    return ans
};
```
```Go []
func countGoodRectangles(rectangles [][]int) (ans int) {
    max := 0
    for _, r := range rectangles {
        cur := min(r[0], r[1])
        if cur > max {
            max = cur
            ans = 1
        } else if cur == max {
            ans++
        }
    }
    return
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}
```
