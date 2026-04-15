# [Python/Java] 从暴力 到 暴力的优化 到 差分 到 并查集?

> Author: Benhao
> Date: 2021-07-23
> Upvotes: 14
> Tags: Java, Python, Python3

---

### 解题思路
暴力就是判断left到right之间每个数是否都有区间覆盖。
暴力的优化：用集合可以统计所有覆盖到的点，避免反复查看同样的区间。
<br>
差分是想到覆盖问题中，在左端点到右端点之间，都是加了1的，到达右端点以后再减一，这样可以保证每次统计都将所有区间的影响加入(如果有被覆盖到必然大于0)
<br>
覆盖问题也想到并查集，覆盖的部分指向它的下一个，没覆盖的指向自己。但是这里效率不大高，可能是数据范围小。

### 代码
```python3
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))
```

```python3
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covers = set()
        for l, r in ranges:
            covers.update({i for i in range(l, r + 1)})
        return all(i in covers for i in range(left, right + 1))
```

```python3 []
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = defaultdict(int)
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        curr = 0
        for i in range(1, right + 1):
            curr += diff[i]
            if curr <= 0 and left <= i:
                return False
        return True

```
```java []
class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        int[] diff = new int[52];
        for(int[] range: ranges){
            int l = range[0], r = range[1] + 1;
            diff[l]++;
            diff[r]--;
        }
        int curr = 0;
        for(int i=1; i<=right; i++){
            curr += diff[i];
            if(i >= left && curr == 0){
                return false;
            }
        }
        return true;
    }
}
```
<br>
```python3 []
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        f = [i for i in range(52)]
        def find(x):
            return x if f[x] == x else find(f[x])
        
        def union(x, y):
            f[find(x)] = find(y)

        for l, r in ranges:
            for i in range(l, r+1):
                union(i, r+1)
        return find(left) > right

```
```java []
class Solution {
    int[] f = new int[52];
    public boolean isCovered(int[][] ranges, int left, int right) {
        for(int i=1;i<52;i++)
            f[i] = i;
        for(int[] range: ranges){
            for(int i=range[0];i<range[1]+1;i++)
                union(i, range[1]+1);
        }
        return find(left) > right;
    }
    
    public int find(int x){
        return f[x] == x ? x : find(f[x]);
    }

    public void union(int x,int y){
        f[find(x)] = find(y);
    }
}
```