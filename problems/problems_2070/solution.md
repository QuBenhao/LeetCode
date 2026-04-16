# [Python/Go] 离线查询

> Author: Benhao
> Date: 2021-11-13
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
排序查询时，当前的结果依赖于上一次查询，可以免去重复的查询

### 代码

```Python3 []
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        qy = []
        for i, q in enumerate(queries):
            heapq.heappush(qy, (q, i))
        items.sort()
        item_idx = 0
        cur = 0
        while qy:
            query, idx = heapq.heappop(qy)
            while item_idx < len(items) and items[item_idx][0] <= query:
                cur = max(cur, items[item_idx][1])
                item_idx += 1
            ans[idx] = cur
        return ans

```
```Go []
func maximumBeauty(items [][]int, queries []int) []int {
    idxMap := map[int][]int{}
    for i, q := range queries {
        idxMap[q] = append(idxMap[q], i)
    }
    sort.Ints(queries)
	sort.Slice(items, func(i, j int) bool {
		if  items[i][0] ==  items[j][0] {
			return items[i][1] < items[j][1]
		}else {
			return items[i][0] < items[j][0]
		}
	})
    ans := make([]int, len(queries))
    for i, j, cur := 0, 0, 0; j < len(queries); j++{
        for ;i < len(items) && items[i][0] <= queries[j];i++ {
            if items[i][1] > cur {
                cur = items[i][1]
            }
        }
        ans[idxMap[queries[j]][0]] = cur
        idxMap[queries[j]] = idxMap[queries[j]][1:]
    }
    return ans
}

```