# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-by-himymben-xj4o
> date: 2022-04-24
> tags: Go, Java, JavaScript, Python, Python3
> question: Random Pick Index (random-pick-index)
> url: https://leetcode.cn/problems/random-pick-index/solutions/C3AJ4R/pythonjavajavascriptgo-by-himymben-xj4o/

---
### 解题思路
暴力模拟就不过多赘述。

[蓄水池算法推荐大家学习一下](https://leetcode.cn/problems/linked-list-random-node/solution/gong-shui-san-xie-xu-shui-chi-chou-yang-1lp9d/)

### 代码

```Python3 []
class Solution:

    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for i, num in enumerate(nums):
            self.map[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```
```Java []
class Solution {
    private Map<Integer, List<Integer>> map;
    private Random random;

    public Solution(int[] nums) {
        map = new HashMap();
        random = new Random();
        for(int i = 0; i < nums.length; i++) {
            List<Integer> list = map.getOrDefault(nums[i], new ArrayList<>());
            list.add(i);
            map.put(nums[i], list);
        }
    }
    
    public int pick(int target) {
        List<Integer> list = map.get(target);
        return list.get(random.nextInt(list.size()));
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```
```JavaScript []
/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    this.map = new Map()
    for(let i = 0; i < nums.length; i++) {
        if(this.map.has(nums[i])) {
            const arr = this.map.get(nums[i])
            arr.push(i)
        } else
            this.map.set(nums[i], [i])
    }
};

/** 
 * @param {number} target
 * @return {number}
 */
Solution.prototype.pick = function(target) {
    const arr = this.map.get(target);
    return arr[Math.floor(Math.random() * arr.length)];
};

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.pick(target)
 */
```
```Go []
type Solution struct {
    Map map[int][]int
}


func Constructor(nums []int) Solution {
    m := map[int][]int{}
    for i, v := range nums {
        m[v] = append(m[v], i)
    }
    return Solution{m}
}


func (this *Solution) Pick(target int) int {
    l := this.Map[target]
    return l[rand.Intn(len(l))]
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Pick(target);
 */
```

```Python3
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans, cnts = -1, 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnts += 1
                if not randrange(cnts):
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```