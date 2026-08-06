# [Python/Java] 暴力枚举中心点

> slug: pythonjava-bao-li-mei-ju-zhong-xin-dian-a21qf
> date: 2021-09-12
> tags: Java, Python, Python3
> question: Number of Boomerangs (number-of-boomerangs)
> url: https://leetcode.cn/problems/number-of-boomerangs/solutions/7EW8je/pythonjava-bao-li-mei-ju-zhong-xin-dian-a21qf/

---
### 解题思路
我们需要知道到任意一个点，距离相等的点(记录不同的距离的个数用哈希表)有哪些。
每$k$个距离相等的点，能选出两个不在乎顺序的可能性为$A_k^2$, 就是$k*(k-1)$

### 代码

```Python3 []
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])

        ans = 0
        for p in points:
            cnts = Counter()
            for q in points:
                cnts[distance(p, q)] += 1
            # 距离到p相等的点(某个距离)有val个，从val个任意取两个不在乎顺序为An2 = n * (n-1)
            for val in cnts.values():
                ans += val * (val - 1)
        return ans
```
```Java []
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int ans = 0, n = points.length;
        for(int i=0;i<n;i++){
            Map<Integer,Integer> cnts = new HashMap<>();
            for(int j=0;j<n;j++){
                int d = distance(points[i][0], points[j][0], points[i][1],points[j][1]);
                int v = cnts.getOrDefault(d, 0);
                cnts.put(d, v+1);
            }
            for(int val: cnts.values())
                ans += val * (val - 1);
        }
        return ans;
    }

    public int distance(int x1, int x2, int y1, int y2){
        return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
    }
}
```

在统计时叠加答案
```Python3 []
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            cnts = defaultdict(int)
            for x2, y2 in points:
                dx, dy = x1 - x2, y1 - y2
                d = dx * dx + dy * dy
                ans += cnts[d]
                cnts[d] += 1
        return ans * 2
```
```Java []
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int ans = 0, n = points.length;
        for(int i = 0; i < n; i++){
            Map<Integer,Integer> cnts = new HashMap<>();
            for(int j = 0; j < n; j++){
                int dx = points[i][0] - points[j][0], dy = points[i][1] - points[j][1];
                int d = dx * dx + dy * dy;
                if(cnts.containsKey(d)){
                    int val = cnts.get(d);
                    ans += val;
                    cnts.put(d, val + 1);
                }else
                    cnts.put(d, 1);
            }
        }
        return ans * 2;
    }
}
```