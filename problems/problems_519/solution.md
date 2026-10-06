# [Python/Java/JavaScript/Go] Flatten the matrix + track swaps in a hash table

> slug: pythonjavajavascriptgo-jiang-wei-ha-xi-b-8ipu
> date: 2021-11-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Random Flip Matrix (random-flip-matrix)
> url: https://leetcode.cn/problems/random-flip-matrix/solutions/kKzjxc/pythonjavajavascriptgo-jiang-wei-ha-xi-b-8ipu/

---
### Approach
Representing a two-dimensional matrix as a one-dimensional array is familiar: use the one-to-one mapping `i,j -> i*n + j`.

After flattening, the approach is identical to the random-number problem from a few days ago. However, m and n can each be $10^4$, giving $10^8$ entries, so maintaining the array is very expensive.
There are at most a thousand calls to flip. Can we record only the used numbers while maintaining the conceptual array above? A hash table comes to mind: instead of swapping entries in a real array, record a mapping from each used position to the value swapped into it.

Suppose the one-dimensional array is [0, 1, 2, 3, 4, 5], with 5 as its last value.
If the first random choice is 3, the next choice should come from [0, 1, 2, 4, 5]. Put `5` in position `3`, effectively swapping `3` and `5`.
The array becomes [0, 1, 2, 5, 4] (record the mapping `3 -> 5`).
For the second random choice, choose an array index in `0~4`. If it is not `3`, repeat the previous operation. If it is `3`, the selected value is effectively `5`. Update the mapping for `3` to the new last value, `4`.
The conceptual array becomes [0, 1, 2, 4] (record the mapping `3` -> `4`); no actual array is created.
Continue until every value has been selected. A used number cannot appear again because its mapping always points to an unused number.

### Code

```python3 []
class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n - 1
        self.record = dict()

    def flip(self) -> List[int]:
        r = random.randint(0, self.total)
        idx = self.record.get(r, r)
        # If the value at total is unused, put that value at idx;
        # Otherwise, use the unused value previously mapped to that position
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
