# [Python/Java] From brute force to optimization, difference arrays, and union-find?

> Author: Benhao
> Date: 2021-07-23
> Upvotes: 14
> Tags: Java, Python, Python3

---

### Approach
Brute force checks whether every number from left through right is covered by an interval.
Optimize it with a set of all covered points, avoiding repeated checks of the same intervals.
<br>
For a difference array, add 1 at each interval's left endpoint and subtract 1 just after its right endpoint. The running total includes every interval's contribution and is positive wherever coverage exists.
<br>
Union-find also fits coverage: covered positions point to the next position, and uncovered positions point to themselves. It is not very efficient here, perhaps because the input range is small.

### Code
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
