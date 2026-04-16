# [Python/Java/TypeScript/Go] 数学

> Author: Benhao
> Date: 2022-07-28
> Upvotes: 34
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
四个点两两的距离一共有6个，
正方形中只有两种距离，一个是边长，一个是对角线，
其中边长出现4次，对角线出现2次，对角线长度是边长的$\sqrt{2}$倍

在数学里的讲法是：
1. 四条边都相等的四边形是菱形。
2. 对角线相等的菱形是正方形。

### 代码

```Python3 []
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return items[0][1] == 4 and items[1][1] == 2 and items[1][0] == 2 * items[0][0] if (dist_cnts := Counter((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 for a, b in itertools.combinations([p1, p2, p3, p4], 2))) and len(items := sorted(dist_cnts.items())) == 2 else False
```
```Java []
class Solution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        Map<Integer, Integer> map = new HashMap<>();
        int[][] points = new int[][]{p1, p2, p3, p4};
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                int d = distance(points[i], points[j]);
                map.put(d, map.getOrDefault(d, 0) + 1);
            }
        }
        if (map.size() != 2) {
            return false;
        }
        int x = Integer.MIN_VALUE, y = 0;
        for (int key: map.keySet()) {
            if (x != Integer.MIN_VALUE) {
                y = key;
            } else {
                x = key;
            }
        }
        if (x > y) {
            int tmp = y;
            y = x;
            x = tmp;
        }
        return y == 2 * x && map.get(x) == 4 && map.get(y) == 2;
    }

    private int distance(int[] p1, int[] p2) {
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]);
    }
}
```
```TypeScript []
function validSquare(p1: number[], p2: number[], p3: number[], p4: number[]): boolean {
    const points: number[][] = [p1, p2, p3, p4], counter: Map<number, number> = new Map<number, number>(), distance = (a: number[], b: number[]): number => {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
    }
    for (let i = 0; i < points.length - 1; i++) {
        for (let j = i + 1; j < points.length; j++) {
            const d = distance(points[i], points[j])
            if (counter.has(d)) {
                counter.set(d, counter.get(d) + 1)
            } else {
                counter.set(d, 1)
            }
        }
    }
    if (counter.size != 2) {
        return false
    }
    let x: number = undefined, y: number
    for (const key of counter.keys()) {
        if (x === undefined) {
            x = key
        } else {
            y = key
        }
    }
    [x, y] = [Math.min(x, y), Math.max(x, y)]
    return y == 2 * x && counter.get(x) == 4 && counter.get(y) == 2
};
```
```Go []
func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
    points, counter, distance := [][]int{p1, p2, p3, p4}, map[int]int{}, func(a []int, b []int) int {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
    }
    for i, n := 0, len(points); i < n - 1; i++ {
        for j := i + 1; j < n; j++ {
            counter[distance(points[i], points[j])] += 1
        }
    }
    if len(counter) != 2 {
        return false
    }
    x, y := int(1E9), 0
    for k, _ := range counter {
        if x == 1E9 {
            x = k
        } else {
            y = k
        }
    }
    if x > y {
        x, y = y, x
    }
    return y == 2 * x && counter[x] == 4 && counter[y] == 2
}
```