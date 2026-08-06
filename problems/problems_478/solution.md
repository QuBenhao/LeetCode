# [Python/Java/TypeScript/Go] 从面积随机 + 极角随机

> slug: pythonjavatypescriptgo-cong-mian-ji-chu-r4yzm
> date: 2022-06-05
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Generate Random Point in a Circle (generate-random-point-in-a-circle)
> url: https://leetcode.cn/problems/generate-random-point-in-a-circle/solutions/DgGVbr/pythonjavatypescriptgo-cong-mian-ji-chu-r4yzm/

---
### 解题思路
已知圆的半径，我们可以清楚知道这个圆的面积。我们从面积随机，根据面积可以反推它到圆心的距离为多少。
这个时候我们的点相当于在一个360度的圆周上，我们同时随机一个角度就能确定一个点。
这两个随机是完全独立的。


注意一些常见的思路的错误之处：
1. 随机一个横坐标，计算纵坐标的范围再随机一个纵坐标。
   主要错误：纵坐标的范围由横坐标决定，不再独立，越靠近圆边缘越密集，圆中心越稀疏。
2. 随机一个极角，再随机一个半径或半径缩放大小。
   主要错误：角度固定后，半径的随机并不应该是均匀的。这样会造成越靠近圆中心越密集，圆边缘稀疏。

### 代码

```Python3 []
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.size = math.pi * radius ** 2

    def randPoint(self) -> List[float]:
        theta, r = random.uniform(0.0, math.pi * 2), sqrt(random.uniform(0.0, self.size) / math.pi)
        return [self.x + math.cos(theta) * r, self.y + math.sin(theta) * r]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```
```Java []
class Solution {
    private Random random;
    private double size, x, y;
    public Solution(double radius, double x_center, double y_center) {
        x = x_center;
        y = y_center;
        size = Math.PI * radius * radius;
        random = new Random();
    }
    
    public double[] randPoint() {
        double theta = random.nextDouble() * 2 * Math.PI, r = Math.sqrt(random.nextDouble() * size / Math.PI);
        return new double[]{x + Math.cos(theta) * r, y + Math.sin(theta) * r};
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * double[] param_1 = obj.randPoint();
 */
```
```TypeScript []
class Solution {
    x: number; y: number; size: number;
    constructor(radius: number, x_center: number, y_center: number) {
        this.x = x_center
        this.y = y_center
        this.size = Math.PI * radius * radius
    }

    randPoint(): number[] {
        const theta = Math.random() * 2 * Math.PI, r = Math.sqrt(Math.random() * this.size / Math.PI)
        return [this.x + Math.cos(theta) * r, this.y + Math.sin(theta) * r]
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(radius, x_center, y_center)
 * var param_1 = obj.randPoint()
 */
```
```Go []
type Solution struct {
    Size, X, Y float64
}


func Constructor(radius float64, x_center float64, y_center float64) Solution {
    return Solution{math.Pi * radius * radius, x_center, y_center}
}


func (this *Solution) RandPoint() []float64 {
    theta, r := rand.Float64() * 2 * math.Pi, math.Sqrt(rand.Float64() * this.Size / math.Pi)
    return []float64{this.X + math.Cos(theta) * r, this.Y + math.Sin(theta) * r}
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(radius, x_center, y_center);
 * param_1 := obj.RandPoint();
 */
```