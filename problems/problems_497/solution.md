# [Python/Java/TypeScript/Go] 前缀和 + 二分

> slug: pythonjavatypescriptgo-qian-zhui-he-er-f-ztcs
> date: 2022-06-09
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Random Point in Non-overlapping Rectangles (random-point-in-non-overlapping-rectangles)
> url: https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/solutions/XAPfm3/pythonjavatypescriptgo-qian-zhui-he-er-f-ztcs/

---
### 解题思路
给定矩形左下角$(a, b)$和右上角$(x, y)$,该矩形内点的个数为$(x - a + 1) \times (y - b + 1)$。
我们可以从全部点的个数中随机一个数，从个数前缀和中确定是在第几个矩阵中。
再从该矩阵的宽或者高，确定随机的点在第几行第几个。

### 代码

```Python3 []
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.presum = [0]
        for a, b, x, y in rects:
            self.presum.append(self.presum[-1] + (x - a + 1) * (y - b + 1))

    def pick(self) -> List[int]:
        rdm = random.randint(0, self.presum[-1] - 1)
        idx = bisect_right(self.presum, rdm) - 1
        a, b, x, y = self.rects[idx]
        v = rdm - self.presum[idx]
        return [a + v % (w := x - a + 1), b + v // w]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
```
```Java []
class Solution {
    private Random random;
    private int[][] rects;
    private int[] presum;
    public Solution(int[][] rects_) {
        random = new Random();
        rects = rects_;
        presum = new int[rects_.length + 1];
        for (int i = 0; i < rects_.length; i++) {
            presum[i + 1] = presum[i] + (rects_[i][2] - rects_[i][0] + 1) * (rects_[i][3] - rects_[i][1] + 1);
        }
    }
    
    public int[] pick() {
        int rdm = random.nextInt(presum[presum.length - 1]);
        int left = 0, right = rects.length;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (presum[mid] > rdm) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        int v = rdm - presum[--left];
        int width = rects[left][2] - rects[left][0] + 1;
        return new int[]{rects[left][0] + (v % width), rects[left][1] + (v / width)};
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.pick();
 */
```
```TypeScript []
class Solution {
    rects: number[][]
    presum: number[]
    constructor(rects: number[][]) {
        this.rects = rects
        this.presum = [0]
        for (const [a, b, x, y] of rects) {
            this.presum.push(this.presum[this.presum.length - 1] + (x - a + 1) * (y - b + 1))
        }
    }

    pick(): number[] {
        const rdm = Math.floor(Math.random() * this.presum[this.presum.length - 1]);
        const idx = this.bineraySearch(rdm) - 1
        const v = rdm - this.presum[idx], [a, b, x, _] = this.rects[idx]
        const width = x - a + 1
        return [a + (v % width), b + Math.floor(v / width)]
    }

    bineraySearch(val: number): number {
        let left = 0, right = this.presum.length
        while (left < right) {
            const mid = (left + right) >> 1
            if (this.presum[mid] > val) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */
```
```Go []
type Solution struct {
    Rects [][]int
    Presum []int
}


func Constructor(rects [][]int) Solution {
    presum := make([]int, len(rects) + 1)
    for i := 0; i < len(rects); i++ {
        presum[i + 1] = presum[i] + (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1)
    }
    return Solution{rects, presum}
}


func (this *Solution) Pick() []int {
    rdm := rand.Intn(this.Presum[len(this.Presum)-1])
    left := 0
    for right := len(this.Presum); left < right; {
        mid := (left + right) >> 1
        if this.Presum[mid] > rdm {
            right = mid
        } else {
            left = mid + 1
        }
    }
    left--
    v := rdm - this.Presum[left]
    a, b, x := this.Rects[left][0], this.Rects[left][1], this.Rects[left][2]
    return []int{a + (v % (x - a + 1)), b + (v / (x - a + 1))}
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(rects);
 * param_1 := obj.Pick();
 */
```