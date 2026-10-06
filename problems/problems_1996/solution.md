# [Python/Java/JavaScript/Go] Sorting and two pointers

> slug: pythonjavajavascriptgo-pai-xu-shuang-zhi-9d9z
> date: 2022-01-28
> tags: Go, Java, JavaScript, Python, Python3
> question: The Number of Weak Characters in the Game (the-number-of-weak-characters-in-the-game)
> url: https://leetcode.cn/problems/the-number-of-weak-characters-in-the-game/solutions/yrsGGK/pythonjavajavascriptgo-pai-xu-shuang-zhi-9d9z/

---
### Approach
A character is weak only if another character has strictly greater attack and defense.
Find strong characters to identify weaker ones; sorting provides a suitable order.
Sort by descending attack, then descending defense. Earlier characters have at least as much attack. Among those with strictly greater attack, track the maximum defense to determine whether the current character is weak.
Use one pointer to mark the current attack group and retain the previous maximum defense. A second pointer scans all characters with that attack, counting those with lower defense.

### Code

```Python3 []
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0], -x[1]))
        ans = max_defense = i = 0
        n = len(properties)
        while i < n:
            j, cur_max, max_defense = i, max_defense, max(max_defense, properties[i][1])
            while j < n and properties[j][0] == properties[i][0]:
                if cur_max > properties[j][1]:
                    ans += 1
                j += 1
            i = j
        return ans
```
```Java []
class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        Arrays.sort(properties, (a,b)->{return a[0] == b[0] ? b[1] - a[1] : b[0] - a[0];});
        int ans = 0;
        for(int i = 0, maxDefense = 0, n = properties.length; i < n;){
            int j = i, cur = maxDefense;
            maxDefense = Math.max(maxDefense, properties[i][1]);
            for(; j < n && properties[j][0] == properties[i][0]; j++)
                if(properties[j][1] < cur)
                    ans++;
            i = j;
        }
        return ans; 
    }
}
```
```JavaScript []
/**
 * @param {number[][]} properties
 * @return {number}
 */
var numberOfWeakCharacters = function(properties) {
    properties.sort((a,b)=>{return a[0] == b[0] ? b[1] - a[1] : b[0] - a[0]})
    const n = properties.length
    let ans = 0
    for(let i = 0, j = 0, maxDefense = 0; i < n; i = j){
        const cur = maxDefense
        maxDefense = Math.max(maxDefense, properties[i][1])
        while(j < n && properties[j][0] == properties[i][0])
            if(properties[j++][1] < cur)
                ans++
    }
    return ans
};
```
```Go []
func numberOfWeakCharacters(properties [][]int) (ans int) {
    sort.Slice(properties, func(i, j int) bool {
        if properties[i][0] == properties[j][0] {
            return properties[j][1] < properties[i][1]
        }
        return properties[j][0] < properties[i][0]
    })
    for i, j, maxDefense, n := 0, 0, 0, len(properties); i < n; i = j {
        for j < n && properties[j][0] == properties[i][0]{
            if properties[j][1] < maxDefense{
                ans++
            }
            j++
        }
        if properties[i][1] > maxDefense {
            maxDefense = properties[i][1]
        }
    }
    return 
}
```
