# [Python/Java/JavaScript/Go] Shuffle algorithm

> slug: pythonjavajavascriptgo-xi-pai-suan-fa-by-k7i2
> date: 2021-11-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Shuffle an Array (shuffle-an-array)
> url: https://leetcode.cn/problems/shuffle-an-array/solutions/7Bt41J/pythonjavajavascriptgo-xi-pai-suan-fa-by-k7i2/

---
### Approach
Choose the value for each position with equal probability.
First, randomly choose an index in `0 ~ n-1` and swap its value into the first position. (Each value is chosen with probability $\frac{1}{n}$.)
From the remaining `n-1` values, randomly choose an index in `1 ~ n-1` and swap its value into the second position. (The probability of not being chosen first and being chosen second is $\frac{n-1}{n} * \frac{1}{n-1} = \frac{1}{n}$.)
。。。
Continue in the same way.
Every value has the same probability, $\frac{1}{n}$, of occupying each position.

### Code

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
