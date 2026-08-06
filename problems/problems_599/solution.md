# [Python/Java/JavaScript/Go] 哈希表

> slug: pythonjavajavascriptgo-ha-xi-biao-by-him-bm8s
> date: 2022-03-13
> tags: Go, Java, JavaScript, Python, Python3
> question: Minimum Index Sum of Two Lists (minimum-index-sum-of-two-lists)
> url: https://leetcode.cn/problems/minimum-index-sum-of-two-lists/solutions/oG8nUW/pythonjavajavascriptgo-ha-xi-biao-by-him-bm8s/

---
### 解题思路
遍历两个列表，记录他们的字符串到坐标的映射，遍历他们的公共字符串，统计坐标和最小的字符串。

### 代码

```Python3 []
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1, d2 = {s:i for i, s in enumerate(list1)}, {s:i for i, s in enumerate(list2)}
        return [c for c in d1.keys() & d2.keys() if d1[c] + d2[c] == v] if (k:=min(d1.keys() & d2.keys(), key=lambda x:d1[x] + d2[x])) and (v := d1[k] + d2[k]) >= 0 else []
```
```Java []
class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String, Integer> map1 = new HashMap<>(), map2 = new HashMap<>();
        for(int i = 0; i < list1.length; i++)
            map1.put(list1[i], i);
        for(int i = 0; i < list2.length; i++)
            map2.put(list2[i], i);
        List<String> ans;
        if(map1.size() < map2.size())
            ans = common(map1, map2);
        else
            ans = common(map2, map1);
        return ans.toArray(new String[ans.size()]);
    }

    private List<String> common(Map<String, Integer> map1, Map<String, Integer>  map2) {
        List<String> ans = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        for(String key: map1.keySet()) {
            if(map2.containsKey(key)) {
                int v = map1.get(key) + map2.get(key);
                if(v < min) {
                    min = v;
                    ans = new ArrayList<>(){{add(key);}};
                } else if (v == min)
                    ans.add(key);
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    const map1 = new Map(), map2 = new Map()
    for(let i = 0; i < list1.length; i++)
        map1.set(list1[i], i)
    for(let i = 0; i < list2.length; i++)
        map2.set(list2[i], i)
    
    helper = function(m1, m2) {
        let res = new Array()
        let min = Number.MAX_SAFE_INTEGER
        for(const k of m1.keys()) {
            if(m2.has(k)) {
                const v = m1.get(k) + m2.get(k)
                if(v < min) {
                    min = v
                    res = [k]
                } else if(v == min)
                    res.push(k)
            }
        }
        return res
    }

    if(map1.size < map2.size)
        return helper(map1, map2)
    return helper(map2, map1)
};
```
```Go []
func findRestaurant(list1 []string, list2 []string) []string {
    map1, map2 := listToIdxMap(list1), listToIdxMap(list2)
    if len(map1) < len(map2) {
        return common(map1, map2)
    }
    return common(map2, map1)
}

func listToIdxMap(list []string) map[string]int {
    res := map[string]int{}
    for i := 0; i < len(list); i++ {
        res[list[i]] = i
    }
    return res
}

func common(m1, m2 map[string]int) (res []string) {
    min := 0x3f3f3f
    for k, v1 := range m1 {
        if v2, ok := m2[k]; ok {
            if v := v1 + v2; v < min {
                min = v
                res = []string{k}
            } else if v == min {
                res = append(res, k)
            }
        }
    }
    return
}
```