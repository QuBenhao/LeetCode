# [Python/Java/TypeScript/Go] 哈希映射

> slug: pythonjavatypescriptgo-by-himymben-2eme
> date: 2022-06-26
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Random Pick with Blacklist (random-pick-with-blacklist)
> url: https://leetcode.cn/problems/random-pick-with-blacklist/solutions/u673fL/pythonjavatypescriptgo-by-himymben-2eme/

---
### 解题思路
值域范围内的个数为n，不可选的数有m个，所以可选的数一共n-m个。
我们随机一个n-m内的数，总能找到唯一一个它对应的可选数。

### 代码

```Python3 []
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.bound = n - m
        self.map = dict()
        i = self.bound
        bset = set(blacklist)
        for black in blacklist:
            if black < self.bound:
                while i in bset:
                    i += 1
                self.map[black] = i
                i += 1

    def pick(self) -> int:
        return self.map.get(r:=randint(0, self.bound - 1), r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
```
```Java []
class Solution {
    private Map<Integer, Integer> map;
    private int bound;
    private Random random;

    public Solution(int n, int[] blacklist) {
        map = new HashMap<>();
        bound = n - blacklist.length;
        random = new Random();
        Set<Integer> set = new HashSet<>();
        for(int black: blacklist) {
            set.add(black);
        }
        int i = bound;
        for (int black: blacklist) {
            if (black < bound) {
                while(set.contains(i)) {
                    i++;
                }
                map.put(black, i++);
            }
        }
    }
    
    public int pick() {
        int r = random.nextInt(bound);
        return map.getOrDefault(r, r);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n, blacklist);
 * int param_1 = obj.pick();
 */
```
```TypeScript []
class Solution {
    bound: number
    map: Map<number, number>
    constructor(n: number, blacklist: number[]) {
        this.bound = n - blacklist.length
        this.map = new Map<number, number>()
        const set = new Set<number>()
        for (const black of blacklist) {
            set.add(black)
        }
        let i = this.bound
        for (const black of blacklist) {
            if (black < this.bound) {
                while (set.has(i)) {
                    i++
                }
                this.map.set(black, i++)
            }
        }
    }

    pick(): number {
        const r = Math.floor(Math.random() * this.bound)
        return this.map.has(r) ? this.map.get(r) : r
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(n, blacklist)
 * var param_1 = obj.pick()
 */
```
```Go []
type Solution struct {
    Bound int
    Map map[int]int
}


func Constructor(n int, blacklist []int) Solution {
    m := len(blacklist)
    mp, set := map[int]int{}, map[int]bool{}
    for _, black := range blacklist {
        set[black] = true
    }
    bound, i := n - m, n - m
    for _, black := range blacklist {
        if black < bound {
            for set[i] {
                i++
            }
            mp[black] = i
            i++
        }
    }
    return Solution{bound, mp}
}


func (this *Solution) Pick() int {
    r := rand.Intn(this.Bound)
    if v, ok := this.Map[r]; ok {
        return v
    }
    return r
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(n, blacklist);
 * param_1 := obj.Pick();
 */
```