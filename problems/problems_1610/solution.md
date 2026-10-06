# [Python/Java/JavaScript/Go] Angles, sorting, and two pointers

> slug: pythonjavajavascriptgo-jiao-du-ji-suan-p-5iy4
> date: 2021-12-15
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Number of Visible Points (maximum-number-of-visible-points)
> url: https://leetcode.cn/problems/maximum-number-of-visible-points/solutions/0ieGGZ/pythonjavajavascriptgo-jiao-du-ji-suan-p-5iy4/

---
### Approach
Computing the angles is a mathematical step: use location as the origin, compute the coordinate differences, use `arctan` to obtain radians, and convert them to degrees.
Sort the resulting points by angle and use two pointers for a sliding window. The largest and smallest angles in the window must differ by at most angle.

Rotate from the first point through all points, tracking the maximum count.

### Code

```Python3 []
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        self.base = 0
        def helper(point):
            dx, dy = point[0] - location[0], point[1] - location[1]
            if not dx and not dy:
                self.base += 1
                return None
            if not dx:
                return 90 if dy > 0 else 270
            if not dy:
                return 0 if dx > 0 else 180
            if dx * dy > 0:
                return math.degrees(math.atan(dy/dx)) + (0 if dx > 0 else 180)
            return math.degrees(math.atan(-dx/dy)) + (90 if dx < 0 else 270)
        
        angles = []
        for p in points:
            degree = helper(p)
            if degree is not None:
                angles.append(degree)
        angles.sort()
        angles = angles + [360 + a for a in angles]
        l = r = ans = 0
        while l < len(angles):
            while r < len(angles) and angles[r] - angles[l] <= angle:
                r += 1
            ans = max(ans, r - l)
            l += 1
        return ans + self.base
```
```Java []
class Solution {
    private int base;
    private int x, y;
    public int visiblePoints(List<List<Integer>> points, int angle, List<Integer> location) {
        base = 0; 
        x = location.get(0); 
        y = location.get(1);
        List<Double> angles = new ArrayList<>();
        for(List<Integer> point: points){
            double degree = helper(point);
            if(degree >= 0)
                angles.add(degree);
        }
        Collections.sort(angles);
        int s = angles.size();
        for(int i=0;i<s;i++)
            angles.add(angles.get(i) + 360);
        int ans = 0;
        for(int l=0,r=0;l<angles.size();l++){
            while(r<angles.size() && angles.get(r) - angles.get(l) <= angle)
                r++;
            ans = Math.max(ans, r - l);
        }
        return ans + base;
    }

    private double helper(List<Integer> point){
        int dx = point.get(0) - x, dy = point.get(1) - y;
        if(dx == 0 && dy == 0){
            base += 1;
            return -1.0;
        }
        if(dx == 0)
            return dy > 0 ? 90.0 : 270.0;
        if(dy == 0)
            return dx > 0 ? 0.0 : 180.0;
        if(dx * dy > 0)
            return Math.toDegrees(Math.atan((double)dy/dx))+(dx > 0 ? 0.0 : 180.0);
        return Math.toDegrees(Math.atan(-(double)dx/dy)) + (dy > 0 ? 90.0 : 270.0);
    }
}
```
```JavaScript []
/**
 * @param {number[][]} points
 * @param {number} angle
 * @param {number[]} location
 * @return {number}
 */
var visiblePoints = function(points, angle, location) {
    let base = 0
    helper = function(point) {
        const dx = point[0] - location[0], dy = point[1] - location[1]
        if(dx == 0 && dy == 0){
            base++
            return undefined
        }
        if(dx == 0)
            return dy > 0 ? 90.0 : 270.0
        if(dy == 0)
            return dx > 0 ? 0.0 : 180.0
        if(dx * dy > 0)
            return Math.atan(dy/dx) * 180.0 / Math.PI + (dx > 0 ? 0.0 : 180.0)
        return Math.atan(-dx/dy) * 180.0 / Math.PI + (dy > 0 ? 90.0 : 270.0)
    }

    const degrees = []
    for(const point of points){
        const d = helper(point)
        if(d !== undefined)
            degrees.push(d)
    }
    degrees.sort((a,b)=>a-b)
    const size = degrees.length
    for(let i=0;i<size;i++)
        degrees.push(degrees[i] + 360.0)
    let ans = 0
    for(let l=0,r=0;l<degrees.length;l++){
        while(r<degrees.length && degrees[r] - degrees[l] <= angle)
            r++
        ans = Math.max(ans, r - l)
    }
    return ans + base
};
```
```Go []
func visiblePoints(points [][]int, angle int, location []int) int {
    ans, base, degrees := 0, 0, []float64{}
    for _, point := range points {
        if d := helper(point, location); d >= 0 {
            degrees = append(degrees, d)
        } else {
            base++
        }
    }
    sort.Float64s(degrees)
    s := len(degrees)
    for i := 0; i < s; i++ {
        degrees = append(degrees, degrees[i] + 360.0)
    }
    diff := float64(angle)
    for l, r := 0, 0; l < s; l++ {
        for r < len(degrees) && degrees[r] - degrees[l] <= diff{
            r++
        }
        if r - l > ans {
            ans = r - l
        }
    }
    return ans + base
}

func helper(points []int, location []int) float64 {
    dx, dy := float64(points[0] - location[0]), float64(points[1] - location[1])
    if dx == 0 && dy == 0 {
        return -1.0
    } else if dx == 0 {
        if dy > 0 {
            return 90.0
        }
        return 270.0
    } else if dy == 0 {
        if dx > 0 {
            return 0.0
        }
        return 180.0
    }

    if dx * dy > 0{
        if dx > 0 {
            return math.Atan(dy/dx) * 180.0 / math.Pi
        }
        return math.Atan(dy/dx) * 180.0 / math.Pi + 180.0
    }
    if dy > 0 {
        return math.Atan(-dx/dy) * 180.0 / math.Pi + 90.0
    }
    return math.Atan(-dx/dy) * 180.0 / math.Pi + 270.0
}
```
