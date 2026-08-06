# [Python/Java/JavaScript/Go] 降维 + 哈希表记录交换

> slug: pythonjavajavascriptgo-jiang-wei-ha-xi-b-8ipu
> date: 2021-11-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Random Flip Matrix (random-flip-matrix)
> url: https://leetcode.cn/problems/random-flip-matrix/solutions/kKzjxc/pythonjavajavascriptgo-jiang-wei-ha-xi-b-8ipu/

---
### 解题思路
二维矩阵用一维数组表示也是老生常谈了，不做赘述了，就是将 `i,j -> i*n + j`做个一对一的映射。

转换成一维其实做法和前几天的随机数的思路是一模一样的。但是有个问题是，m和n都是$10^4$，乘起来是$10^8$，这样的数组维护起来是极其昂贵的。
注意到最多flip一千次，那么有没有办法可以只记录用过的数，并维护出上面我们想要的数组的样子呢？首先想到的就是哈希表了，既然没有数组去交换记录，是不是可以直接记录被用的数和他交换的数的映射呢？

假设我们的一维数组为 [0, 1, 2, 3, 4, 5]，最后一个值为5；
第一次random，假如是3，我们下一次随机是想要[0, 1, 2, 4, 5]中取一个，将`5`填入`3`的位置，就像是做了一次`3`和`5`的交换，
数组变为 [0, 1, 2, 5, 4] （我们记录映射 `3 -> 5`）
第二次random，我们在`0~4`中取一个（数组坐标），假如不是`3`，我们做和上一次一样的操作；假如是`3`，那么我们这次随机出来的数就相当于是`5`，这个时候我们仍需要将`3`的映射更新，变为最新的最后一个数`4`，
这样数组就变为 [0, 1, 2, 4] (我们记录映射 `3` -> `4`)，并不是真的做了这么个数组。
一直到最后将全部数组都可以随机出，被用过的数不会再出现，因为始终会取它们映射到的没被用过的数。

### 代码

```python3 []
class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n - 1
        self.record = dict()

    def flip(self) -> List[int]:
        r = random.randint(0, self.total)
        idx = self.record.get(r, r)
        # 相当于total的值没被用，将那个值填入idx位置；
        # 被用了的话，将它那里填入的没被用的值填入
        self.record[r] = self.record.get(self.total, self.total)
        self.total -= 1
        ans = [idx // self.n, idx % self.n]
        return ans

    def reset(self) -> None:
        self.total = self.m * self.n - 1
        self.record = dict()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
```
```Java []
class Solution {
    private int m, n, total;
    private Map<Integer, Integer> map = new HashMap<>();
    private Random random;
    public Solution(int m, int n) {
        this.m = m;
        this.n = n;
        total = m * n - 1;
        map = new HashMap<>();
        random = new Random();
    }
    
    public int[] flip() {
        int r = random.nextInt(total + 1);
        int idx = map.getOrDefault(r, r);
        map.put(r, map.getOrDefault(total, total));
        total--;
        return new int[]{idx/n, idx%n};
    }
    
    public void reset() {
        total = m * n - 1;
        map = new HashMap<>();
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(m, n);
 * int[] param_1 = obj.flip();
 * obj.reset();
 */
```
```JavaScript []
/**
 * @param {number} m
 * @param {number} n
 */
var Solution = function(m, n) {
    this.m = m
    this.n = n
    this.total = m * n - 1
    this.map = new Map()
};

/**
 * @return {number[]}
 */
Solution.prototype.flip = function() {
    const r = Math.floor(Math.random() * (this.total + 1))
    const idx = this.map.has(r) ? this.map.get(r) : r
    this.map.set(r, this.map.has(this.total) ? this.map.get(this.total) : this.total)
    this.total--
    return [Math.floor(idx/this.n), idx%this.n]  
};

/**
 * @return {void}
 */
Solution.prototype.reset = function() {
    this.total = this.m *  this.n - 1
    this.map = new Map()
};

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(m, n)
 * var param_1 = obj.flip()
 * obj.reset()
 */
```
```Go []
type Solution struct {
    m, n, total int
    d map[int]int
}


func Constructor(m int, n int) Solution {
    return Solution{m, n, m * n - 1, map[int]int{}}
}


func (this *Solution) Flip() []int {
    r := rand.Intn(this.total + 1)
    idx, ok := this.d[r]
    if !ok {
        idx = r
    }
    if v, okay := this.d[this.total]; okay {
        this.d[r] = v
    } else {
        this.d[r] = this.total
    }
    this.total--
    return []int{idx/this.n,idx%this.n}
}


func (this *Solution) Reset()  {
    this.total = this.m * this.n - 1
    this.d = map[int]int{}
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(m, n);
 * param_1 := obj.Flip();
 * obj.Reset();
 */
```