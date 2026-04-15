# [Python/Go] 取余模拟

> Author: Benhao
> Date: 2021-11-13
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
按周长取余，并分情况讨论属于哪个边

### 代码

```Python3 []
class Robot:

    def __init__(self, width: int, height: int):
        self.m = height
        self.n = width
        self.x = self.y = self.dir = self.cur = 0
        self.dirs = ["East", "North", "West", "South"]

    def move(self, num: int) -> None:
        def findL(x, y):
            if x == 0:
                return y
            elif y == n-1:
                return x + y
            elif x == m-1:
                return m + n + n - 3 - y
            else:
                return (m + n) * 2 - 4 - x

        m, n = self.m, self.n
        self.cur = (self.cur + num) % (2 * (m + n) - 4)
        length = self.cur
        if length < n:
            self.x, self.y = 0, length
            if length:
                self.dir = 0
            else:
                self.dir = 3
        elif length < m + n - 1:
            self.x, self.y = length - n + 1, n-1
            self.dir = 1
        elif length < m + n * 2 - 2:
            self.x, self.y = m - 1, m + 2 * n - 3 - length
            self.dir = 2
        else:
            self.x, self.y = 2 * m + 2 * n - 4 - length, 0
            self.dir = 3

    def getPos(self) -> List[int]:
        return [self.y, self.x]

    def getDir(self) -> str:
        #"North" ，"East" ，"South" 或者 "West"
        return self.dirs[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
```
```Go []
type Robot struct {
    m int
    n int
    x int
    y int
    cur int
    dir int
}


func Constructor(width int, height int) Robot {
    return Robot{m:height, n:width}
}


func (this *Robot) Move(num int)  {
    l := this.m * 2 + this.n * 2 - 4
    this.cur = (this.cur + num) % l
    if this.cur < this.n {
        this.x, this.y = 0, this.cur
        if this.cur > 0 {
            this.dir = 0
        } else {
            this.dir = 3
        }
    } else if this.cur < this.m + this.n - 1 {
        this.x, this.y = this.cur - this.n + 1, this.n - 1
        this.dir = 1
    } else if this.cur < this.m + this.n * 2 - 2 {
        this.x, this.y = this.m - 1, this.m + this.n * 2 - 3 - this.cur
        this.dir = 2
    } else {
        this.x, this.y =  this.m * 2 + this.n * 2 - 4 - this.cur, 0
        this.dir = 3
    }
}


func (this *Robot) GetPos() []int {
    return []int{this.y, this.x}
}


func (this *Robot) GetDir() string {
    return []string{"East", "North", "West", "South"}[this.dir]
}


/**
 * Your Robot object will be instantiated and called as such:
 * obj := Constructor(width, height);
 * obj.Move(num);
 * param_2 := obj.GetPos();
 * param_3 := obj.GetDir();
 */
```