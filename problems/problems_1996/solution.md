# [Python/Java/JavaScript/Go] 排序双指针

> slug: pythonjavajavascriptgo-pai-xu-shuang-zhi-9d9z
> date: 2022-01-28
> tags: Go, Java, JavaScript, Python, Python3
> question: The Number of Weak Characters in the Game (the-number-of-weak-characters-in-the-game)
> url: https://leetcode.cn/problems/the-number-of-weak-characters-in-the-game/solutions/yrsGGK/pythonjavajavascriptgo-pai-xu-shuang-zhi-9d9z/

---
### 解题思路
本题要求攻击、防御两个纬度都超杀，才能判断一个角色是弱角色。
我们想知道尽可能强的怪，用来判断其他弱的怪。容易满足这个想法的是排序。
按攻击从大到小、防御从大到小排序后，我们得到一个比较满意的顺序，遍历到当前的指针时，之前的怪的攻击力都是大于等于自己的，我们只需要知道他们之中大于自己攻击力的最高的防御力，来确认自己是不是弱角色。
使用双指针，第一个指针维护当前遍历到的攻击力（之前最高的防御力），第二个指针遍历与第一个指针攻击力相同的怪的防御力（当前攻击力下的防御力），统计弱角色的个数。

### 代码

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