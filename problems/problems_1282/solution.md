# [Python/Java/TypeScript/Go] Simple simulation

> Author: Benhao
> Date: 2022-08-11
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Group people by their required group size, then split each bucket into groups of that size.

PS:
An optimal approach (can beat 100%): construct groups during the traversal.

### Code

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

```python3 [v1-One traversal Python3]
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
```go [v1-One traversal Go]
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
