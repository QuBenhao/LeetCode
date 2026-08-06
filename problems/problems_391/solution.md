# [Python/Java/JavaScript/Go] 统计每个点出现次数以及矩形面积和

> slug: pythonjavajavascriptgo-tong-ji-mei-ge-di-x3ub
> date: 2021-11-15
> tags: Go, Java, JavaScript, Python, Python3
> question: Perfect Rectangle (perfect-rectangle)
> url: https://leetcode.cn/problems/perfect-rectangle/solutions/wmFKN9/pythonjavajavascriptgo-tong-ji-mei-ge-di-x3ub/

---
### 解题思路
我们考虑拼出完美矩形的情况:
1. 左下角、左上角、右下角、右上角的顶点一定是所有矩阵的最外圈
2. 它们的`面积和`一定和完美矩阵的面积相等
3. 任意不是这四个顶点的小矩阵的点，一定会出现两次或四次（如果出现四次以上，一定有超过四个矩阵以这个点为顶点，那么必然有重叠；如果出现奇数次，那么必然没有被完整覆盖）【这个的判断可以去掉面积相等，但是是内部重叠的情况】

### 代码

```Python3 []
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x, y, a, b, s = inf, inf, -inf, -inf, 0
        cnts = Counter()
        for x_, y_, a_, b_ in rectangles:
            x, y, a, b = min(x, x_), min(y, y_), max(a, a_), max(b, b_)
            s += (a_ - x_) * (b_ - y_)
            cnts[(x_, y_)] += 1
            cnts[(a_, b_)] += 1
            cnts[(x_, b_)] += 1
            cnts[(a_, y_)] += 1
        if s != (a - x) * (b - y):
            return False
        ps = {(x, y), (x, b), (a, y), (a, b)}
        for p in ps:
            if cnts[p] != 1:
                return False
        for i, v in cnts.items():
            if v > 4 or (i not in ps and v % 2):
                return False
        return True
```
```Java []
class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        int x = 10001, y = 10001, a = -10001, b = -10001;
        long s = 0;
        Map<String, Integer> cnts = new HashMap<>();
        for(int[] r: rectangles){
            x = Math.min(x, r[0]);
            y = Math.min(y, r[1]);
            a = Math.max(a, r[2]);
            b = Math.max(b, r[3]);
            s += (r[3] - r[1]) * (r[2] - r[0]);
            String p1 = point(r[0], r[1]), p2 = point(r[0],r[3]), p3 = point(r[2], r[1]), p4 = point(r[2],r[3]);
            cnts.put(p1, cnts.getOrDefault(p1, 0) + 1);
            cnts.put(p2, cnts.getOrDefault(p2, 0) + 1);
            cnts.put(p3, cnts.getOrDefault(p3, 0) + 1);
            cnts.put(p4, cnts.getOrDefault(p4, 0) + 1);
        }
        if(s != (a - x) * (b - y))
            return false;
        Set<String> points = new HashSet<>(){};
        points.add(point(x, y)); 
        points.add(point(x, b));
        points.add(point(a, y));
        points.add(point(a, b));
        for(String p:points){
            if(!cnts.containsKey(p) || cnts.get(p) != 1)
                return false;
        }
        for(String p:cnts.keySet()){
            if(!points.contains(p)){
                int v = cnts.get(p);
                if(v > 4 || v % 2 != 0)
                    return false;
            }
        }
        return true;
    }

    private String point(int x, int y){
        return String.format("%d,%d",x,y);
    }
}
```
```JavaScript []
/**
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var point = function(x, y){
    return 10001 * x + y;
}

var isRectangleCover = function(rectangles) {
    let x = 10001, y = 10001, a = -10001, b = -10001, s = 0;
    cnts = new Map();
    for(const r of rectangles){
        x = Math.min(x, r[0]);
        y = Math.min(y, r[1]);
        a = Math.max(a, r[2]);
        b = Math.max(b, r[3]);
        s += (r[3] - r[1]) * (r[2] - r[0]);
        const p1 = point(r[0], r[1]), p2 = point(r[0],r[3]), p3 = point(r[2], r[1]), p4 = point(r[2],r[3]);
        if(cnts.has(p1))
            cnts.set(p1, cnts.get(p1) + 1);
        else
            cnts.set(p1, 1);
        if(cnts.has(p2))
            cnts.set(p2, cnts.get(p2) + 1);
        else
            cnts.set(p2, 1);
        if(cnts.has(p3))
            cnts.set(p3, cnts.get(p3) + 1);
        else
            cnts.set(p3, 1);
        if(cnts.has(p4))
            cnts.set(p4, cnts.get(p4) + 1);
        else
            cnts.set(p4, 1);
    }
    if(s != (a - x) * (b - y))
        return false;
    const points = new Set();
    points.add(point(x, y)); 
    points.add(point(x, b));
    points.add(point(a, y));
    points.add(point(a, b));
    for(const p of points){
        if(!cnts.has(p) || cnts.get(p) != 1){
            return false;
        }
    }
    for(const p of cnts.keys()){
        if(!points.has(p)){
            const v = cnts.get(p);
            if(v > 4 || v % 2 != 0)
                return false;
        }
    }
    return true;
};
```
```Go []
func isRectangleCover(rectangles [][]int) bool {
    x, y, a, b, s := 10001, 10001, -10001, -10001, 0
    cnts := map[int]int{}
    for _, r := range rectangles {
        x, y, a, b = min(x, r[0]), min(y, r[1]), max(a, r[2]), max(b, r[3])
        s += (r[2] - r[0]) * (r[3] - r[1])
        cnts[point(r[0], r[1])] += 1
        cnts[point(r[0], r[3])] += 1
        cnts[point(r[2], r[1])] += 1
        cnts[point(r[2], r[3])] += 1
    }
    if s != (a - x) * (b - y) {
        return false
    }
    points := map[int]bool{}
    points[point(x, y)] = true
    points[point(x, b)] = true
    points[point(a, y)] = true
    points[point(a, b)] = true
    for p := range points {
        v, err := cnts[p]
        if !err || v > 1 {
            return false
        }
    }
    for p, v := range cnts {
        if !points[p] {
            if v > 4 || v % 2 == 1{
                return false
            }
        }
    }
    return true
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func point(a, b int) int {
    return 10001 * a + b
}
```
两两相消
```Python3 []
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        s, points = 0, set()
        for x, y, a, b in rectangles:
            s += (a - x) * (b - y)
            points.symmetric_difference_update({(x,y), (a,b),(x,b),(a,y)})
        return len(points) == 4 and s == (max((l:=list(zip(*points)))[0]) - min(l[0])) * (max(l[1]) - min(l[1]))
```
```Go []
type point struct{
    x int
    y int
}
func isRectangleCover(rectangles [][]int) bool {
    s := 0
    points := map[point]bool{}
    for _, r := range rectangles {
        s += (r[2] - r[0]) * (r[3] - r[1])
        p1, p2, p3, p4 := point{r[0], r[1]}, point{r[0], r[3]}, point{r[2], r[1]}, point{r[2], r[3]}
        addOrRemove(points, p1)
        addOrRemove(points, p2)
        addOrRemove(points, p3)
        addOrRemove(points, p4)
    }
    if len(points) != 4 {
        return false
    }
    x, y, a, b := 10001, 10001, -10001, -10001
    for p := range points {
        x, y, a, b = min(x, p.x), min(y, p.y), max(a, p.x), max(b, p.y)
    }
    return s == (a - x) * (b - y)
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func addOrRemove(points map[point]bool,p point){
    _, ok := points[p]
    if ok {
        delete(points, p)
    } else{
        points[p] = true
    }
}
```