# [Python/Java/JavaScript/Go] 排序 + 双指针

> slug: pythonjavajavascriptgo-pai-xu-shuang-zhi-p76s
> date: 2021-12-19
> tags: Go, Java, JavaScript, Python, Python3
> question: Heaters (heaters)
> url: https://leetcode.cn/problems/heaters/solutions/eHtAMR/pythonjavajavascriptgo-pai-xu-shuang-zhi-p76s/

---
### 解题思路
其实就是要找每个房子落在哪个加热器之间，然后比较他们俩之中更近的那一侧。可以使用二分，也可以使用双指针，从头开始一起移动。

### 代码

```Python3 []
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = heaters + [-inf, inf]
        houses.sort()
        heaters.sort()
        i, j, ans = 0, 0, 0
        while i < len(houses):
            cur = inf
            while heaters[j] <= houses[i]:
                cur = houses[i] - heaters[j]
                j += 1
            cur = min(cur, heaters[j] - houses[i])
            ans = max(cur, ans)
            i += 1
            j -= 1
        return ans
```
```Java []
class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(houses);
        Arrays.sort(heaters);
        int ans = 0;
        for(int i=0, j=0; i < houses.length; i++) {
            int cur = Math.abs(heaters[j] - houses[i]);
            while(j < heaters.length && heaters[j] <= houses[i]){
                cur = houses[i] - heaters[j++];
            }
            if(j < heaters.length)
                cur = Math.min(cur, Math.abs(heaters[j] - houses[i]));
            ans = Math.max(ans, cur);
            if(j > 0)
                j--;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} houses
 * @param {number[]} heaters
 * @return {number}
 */
var findRadius = function(houses, heaters) {
    houses.sort((a,b)=>a-b)
    heaters.sort((a,b)=>a-b)
    let ans = 0
    for(let i=0, j=0; i < houses.length; i++){
        let cur = Math.abs(houses[i] - heaters[j])
        while(j < heaters.length && heaters[j] <= houses[i])
            cur = houses[i] - heaters[j++]
        if(j < heaters.length)
            cur = Math.min(cur, heaters[j] - houses[i])
        ans = Math.max(ans, cur)
        if(j > 0)
            j--
    }
    return ans
};
```
```Go []
func findRadius(houses []int, heaters []int) int {
    sort.Ints(houses)
    sort.Ints(heaters)
    ans := 0
    for i, j := 0, 0; i < len(houses); i++ {
        cur := absDiff(houses[i], heaters[j])
        for j < len(heaters) && heaters[j] <= houses[i]{
            cur = houses[i] - heaters[j]
            j++
        }
        if j < len(heaters) {
            if v := heaters[j] - houses[i]; v < cur {
                cur = v
            }
        }
        if cur > ans {
            ans = cur
        }
        if j > 0 {
            j--
        }
    }
    return ans
}

func absDiff(a, b int) int {
    if a > b {
        return a - b
    }
    return b - a
}
```