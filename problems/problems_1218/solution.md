# [Python/Java/JavaScript/Go] Dynamic programming

> slug: pythonjavajavascriptgo-dong-tai-gui-hua-jypcp
> date: 2021-11-04
> tags: Go, Java, JavaScript, Python, Python3
> question: Longest Arithmetic Subsequence of Given Difference (longest-arithmetic-subsequence-of-given-difference)
> url: https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/solutions/VzqKjM/pythonjavajavascriptgo-dong-tai-gui-hua-jypcp/

---
### Approach
The longest fixed-difference subsequence ending at `num` is determined by the length of the longest such subsequence ending at the earlier value `num-difference`.

### Code

```Python3 []
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = defaultdict(int)
        for num in arr:
            d[num] = d[num - difference] + 1
        return max(d.values())
```
```Java []
class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 1;
        for(int num:arr){
            int val = map.getOrDefault(num-difference,0);
            map.put(num, ++val);
            ans = Math.max(ans, val);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} arr
 * @param {number} difference
 * @return {number}
 */
var longestSubsequence = function(arr, difference) {
    const map = new Map();
    let ans = 1;
    for(const num of arr){
        if(map.has(num - difference)){
            const v = map.get(num-difference) + 1;
            map.set(num, v);
            ans = Math.max(ans, v);
        }else
            map.set(num, 1);
    }
    return ans;
};
```
```Go []
func longestSubsequence(arr []int, difference int) int {
    d, result := map[int](int){}, 1
    for _, num := range arr {
        d[num] = d[num - difference] + 1;
        if d[num] > result { 
            result = d[num]
        }
    }
    return result
}
```
