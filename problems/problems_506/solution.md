# [Python/Java/JavaScript/Go] 哈希表 + 排序

> slug: pythonjavajavascriptgo-ha-xi-biao-pai-xu-xfg9
> date: 2021-12-01
> tags: Go, Java, JavaScript, Python, Python3
> question: Relative Ranks (relative-ranks)
> url: https://leetcode.cn/problems/relative-ranks/solutions/Z5DN0G/pythonjavajavascriptgo-ha-xi-biao-pai-xu-xfg9/

---
### 解题思路
哈希表记录原来的分值对应的坐标，这样排序后我们就知道每个原来的坐标排多少名了。

### 代码

```python3 []
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans, d = [None] * len(score), dict()
        for i, num in enumerate(score):
            d[num] = i
        score.sort(reverse=True)
        for i, num in enumerate(score, 1):
            if i <= 3:
                ans[d[num]] = ["", "Gold Medal","Silver Medal","Bronze Medal"][i]
            else:
                ans[d[num]] = str(i)
        return ans
```
```Java []
class Solution {
    private static final String[] SSP = new String[]{"Gold Medal","Silver Medal","Bronze Medal"};
    public String[] findRelativeRanks(int[] score) {
        Map<Integer, Integer> map = new HashMap<>();
        String[] ans = new String[score.length];
        for(int i=0;i<score.length;i++)
            map.put(score[i], i);
        Arrays.sort(score);
        for(int i=0;i<score.length;i++){
            int j = score.length - 1 - i;
            ans[map.get(score[i])] = j <= 2 ?  SSP[j] : (j + 1) + "";
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} score
 * @return {string[]}
 */
const SSP = ["Gold Medal","Silver Medal","Bronze Medal"]
var findRelativeRanks = function(score) {
    const map = new Map(), ans = new Array(score.length);
    for(let i=0;i<score.length;i++)
        map.set(score[i], i)
    score = score.sort((a,b)=>b-a)
    for(let i=0;i<score.length;i++)
        ans[map.get(score[i])] = i <= 2 ? SSP[i] : (i + 1) + ""
    return ans
};
```
```Go []
func findRelativeRanks(score []int) []string {
    ssp := []string{"Gold Medal","Silver Medal","Bronze Medal"}
    m, ans := make(map[int]int), make([]string, len(score))
    for i := 0; i < len(score); i++ {
        m[score[i]] = i
    }
    sort.Slice(score, func(a, b int) bool {return score[b] < score[a]})
    for i := 0; i < len(score); i++ {
        if i <= 2{
            ans[m[score[i]]] = ssp[i]
        }else {
            ans[m[score[i]]] = strconv.Itoa(i + 1)
        }
    }
    return ans
}
```