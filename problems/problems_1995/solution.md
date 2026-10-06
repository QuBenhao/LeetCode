# [Python/Java/JavaScript/Go] Two Sum idea or knapsack DP

> slug: pythonjavajavascriptgo-liang-shu-zhi-he-optkq
> date: 2021-12-28
> tags: Go, Java, JavaScript, Python, Python3
> question: Count Special Quadruplets (count-special-quadruplets)
> url: https://leetcode.cn/problems/count-special-quadruplets/solutions/4iAc7p/pythonjavajavascriptgo-liang-shu-zhi-he-optkq/

---
### Approach
This resembles LeetCode's classic first problem. Enumerate pair sums on the left and pair differences on the right, dynamically adding matching counts to the answer.

Alternatively, use knapsack DP to choose three values. Maintain counts of each sum with zero, one, two, or three values selected.
At each number, add the count of three-value sums equal to that number to the answer.

### Code

```Python3 []
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        l, ans = Counter(), 0
        for i in range(1, len(nums) - 2):
            # All pair sums from indices 0 through i have been counted
            for j in range(i):
                l[nums[i] + nums[j]] += 1
            # The third index is i+1; enumerate possible fourth indices j
            for j in range(i + 2, len(nums)):
                # Add the previously counted left-pair sums matching this third index i+1 and fourth index j
                ans += l[nums[j] - nums[i+1]]
        return ans
```
```Java []
class Solution {
    public int countQuadruplets(int[] nums) {
        Map<Integer, Integer> cnts = new HashMap<>();
        int ans = 0;
        for(int i=1;i<nums.length-2;i++){
            for(int j=0;j<i;j++)
                cnts.put(nums[i] + nums[j], cnts.getOrDefault(nums[i] + nums[j], 0) + 1);
            for(int j=i+2;j<nums.length;j++)
                if(cnts.containsKey(nums[j] - nums[i+1]))
                    ans += cnts.get(nums[j] - nums[i+1]);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const cnts = new Map()
    let ans = 0
    for(let i=1;i<nums.length-2;i++){
        for(let j=0;j<i;j++)
            if(cnts.has(nums[i] + nums[j]))
                cnts.set(nums[i] + nums[j], cnts.get(nums[i] + nums[j]) + 1)
            else
                cnts.set(nums[i] + nums[j], 1)
        for(let j=i+2;j<nums.length;j++)
            if(cnts.has(nums[j] - nums[i+1]))
                ans += cnts.get(nums[j] - nums[i+1])
    }
    return ans
};
```
```Go []
func countQuadruplets(nums []int) (ans int) {
    cnts := map[int]int{}
    for i := 1; i < len(nums) - 2; i++ {
        for j := 0; j < i; j++{
            cnts[nums[i] + nums[j]]++
        }
        for j := i + 2; j < len(nums); j++ {
            ans += cnts[nums[j] - nums[i+1]]
        }
    }
    return
}
```
---
```Python3 []
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        dp, ans = [[0] * 101 for _ in range(4)], 0
        dp[0][0] = 1
        for num in nums:
            ans += dp[3][num]
            for j in range(3, 0, -1):
                for i in range(num, len(dp[0])):
                    dp[j][i] += dp[j-1][i-num]
        return ans
```
```Java []
class Solution {
    public int countQuadruplets(int[] nums) {
        int[][] dp = new int[4][101];
        dp[0][0] = 1;
        int ans = 0;
        for(int num: nums){
            ans += dp[3][num];
            for(int j=dp.length-1;j>0;j--)
                for(int i=num;i<dp[0].length;i++)
                    dp[j][i] += dp[j-1][i-num];
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const dp = Array.from(new Array(4), () => new Array(101).fill(0))
    dp[0][0] = 1
    let ans = 0
    for(const num of nums){
        ans += dp[3][num]
        for(let i=dp.length-1;i>0;i--)
            for(let j=num;j<dp[0].length;j++)
                dp[i][j] += dp[i-1][j-num]
    }
    return ans
};
```
```Go []
func countQuadruplets(nums []int) (ans int) {
    dp := make([][]int, 4)
    for i:=0;i<4;i++{
        dp[i] = make([]int, 101)
    }
    dp[0][0] = 1
    for _, num := range nums {
        ans += dp[3][num]
        for i:=3;i>0;i--{
            for j:=num;j<101;j++{
                dp[i][j] += dp[i-1][j-num]
            }
        }
    }
    return
}
```

### Complexity

Time complexity: $o(n^{2})$
