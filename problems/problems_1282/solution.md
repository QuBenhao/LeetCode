# [Python/Java/TypeScript/Go] 简单模拟

> Author: Benhao
> Date: 2022-08-11
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
按所在组人数分组，每个组是所在组人数的人就行

PS:
最优解法（可达100%），可以在遍历中构造

### 代码

```Python3 []
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp, ans = defaultdict(list), []
        for i, v in enumerate(groupSizes):
            mp[v].append(i)
        for k, lt in mp.items():
            ans.extend(lt[i:i+k] for i in range(0, len(lt), k))
        return ans
```
```Java []
class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < groupSizes.length; i++) {
            List<Integer> list = map.getOrDefault(groupSizes[i], new ArrayList<>());
            list.add(i);
            map.put(groupSizes[i], list);
        }
        map.forEach((k, list) -> {
            for (int i = 0; i < list.size(); i += k) {
                ans.add(list.subList(i, i + k));
            }
        });
        return ans;
    }
}
```
```TypeScript []
function groupThePeople(groupSizes: number[]): number[][] {
    const map: Map<number,number[]> = new Map<number,number[]>(), ans: number[][] = new Array<number[]>()
    for (const [i, v] of groupSizes.entries()) {
        if (!map.has(v)) {
            map.set(v, new Array<number>())
        }
        map.get(v).push(i)
    }
    map.forEach((v, k) => {
        for (let i = 0; i < v.length; i+=k) {
            ans.push(v.slice(i, i + k))
        }
    })
    return ans
};
```
```Go []
func groupThePeople(groupSizes []int) (ans [][]int) {
    mp := map[int][]int{}
    for i, v := range groupSizes {
        mp[v] = append(mp[v], i)
    }
    for k, v := range mp {
        for i := 0; i < len(v); i += k {
            ans = append(ans, v[i:i + k])
        }
    }
    return
}
```

```python3 [v1-一次遍历 Python3]
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans, mp = [], dict()
        for i, v in enumerate(groupSizes):
            if not v in mp or len(ans[mp[v]]) == v:
                mp[v] = len(ans)
                ans.append([i])
            else:
                ans[mp[v]].append(i)
        return ans
```
```go [v1-一次遍历 Go]
func groupThePeople(groupSizes []int) (ans [][]int) {
    mp := map[int]int{}
    for i, v := range groupSizes {
        if val, ok := mp[v]; !ok || len(ans[val]) == v {
            mp[v] = len(ans)
            ans = append(ans, []int{i})
        } else {
            ans[val] = append(ans[val], i)
        }
    }
    return
}
```