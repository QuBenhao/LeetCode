# [Python/Java/JavaScript/Go] 洗牌算法

> slug: pythonjavajavascriptgo-xi-pai-suan-fa-by-k7i2
> date: 2021-11-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Shuffle an Array (shuffle-an-array)
> url: https://leetcode.cn/problems/shuffle-an-array/solutions/7Bt41J/pythonjavajavascriptgo-xi-pai-suan-fa-by-k7i2/

---
### 解题思路
等概率选择每个位置应该填哪个数。
具体来说，我们先在`0 ~ n-1`中随机选一个坐标，将它作为第一个，和第一个交换位置； （每个数被选到的概率是 $\frac{1}{n}$）
剩下的`n-1`个数里，继续随机一个`1 ~ n-1`的坐标，将它作为第二个，和第二个交换位置；(每个数被选到的概率为第一次没被选到且第二次被选到 $\frac{n-1}{n} * \frac{1}{n-1} = \frac{1}{n}$)
。。。
以此类推。
每个数填到每个位置是等概率的，都是$\frac{1}{n}$

### 代码

```python3 []
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        self.temp = list(self.nums)
        for i in range(len(self.nums)):
            idx = random.randint(i, len(self.nums) - 1)
            self.temp[i], self.temp[idx] = self.temp[idx], self.temp[i]
        return self.temp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```
```Java []
class Solution {
    private int[] nums;
    private Random random;

    public Solution(int[] nums) {
        this.nums = nums;
        random = new Random();
    }
    
    public int[] reset() {
        return nums;
    }
    
    public int[] shuffle() {
        int[] temp = Arrays.copyOf(nums, nums.length);
        for(int i=0;i<temp.length;i++){
            int idx = random.nextInt(temp.length-i) + i;
            int tmp = temp[idx];
            temp[idx] = temp[i];
            temp[i] = tmp;
        }
        return temp;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
```
```JavaScript []
/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    this.nums = nums;
};

/**
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    return this.nums;
};

/**
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
    const temp = this.nums.concat();
    for(let i=0;i<temp.length;i++){
        const idx = Math.floor(Math.random() * (temp.length-i)) + i;
        const tmp = temp[idx];
        temp[idx] = temp[i];
        temp[i] = tmp;
    }
    return temp;
};

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
```
```Go []
type Solution struct {
    nums []int
}


func Constructor(nums []int) Solution {
    s := Solution{nums}
    return s
}


func (this *Solution) Reset() []int {
    return this.nums
}


func (this *Solution) Shuffle() []int {
    temp := make([]int, len(this.nums))
    copy(temp, this.nums)
    for i := 0; i < len(temp); i++ {
        idx := rand.Intn(len(temp) - i) + i
        temp[i], temp[idx] = temp[idx], temp[i]
    }
    return temp
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
```