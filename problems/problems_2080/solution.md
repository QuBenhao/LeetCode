# [Python/Go] 哈希表+二分

> Author: Benhao
> Date: 2021-11-21
> Upvotes: 3
> Tags: Go, Python, Python3

---

### 解题思路
模拟即可

### 代码

```python3 []
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.cnts = defaultdict(list)
        for i,num in enumerate(arr):
            self.cnts[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.cnts[value],right) - bisect_left(self.cnts[value],left)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```
```Go []
type RangeFreqQuery struct {
    m map[int]sort.IntSlice
}


func Constructor(arr []int) RangeFreqQuery {
    r := RangeFreqQuery{m:map[int]sort.IntSlice{}}
    for i, num := range arr {
        r.m[num] = append(r.m[num], i)
    }
    return r
}


func (this *RangeFreqQuery) Query(left int, right int, value int) int {
    cur := this.m[value]
    return cur[cur.Search(left):].Search(right + 1)
}


/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,value);
 */
```