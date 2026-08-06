# [Python/Java/JavaScript/Go] 两数之和思想 or 背包动态规划

> slug: pythonjavajavascriptgo-liang-shu-zhi-he-optkq
> date: 2021-12-28
> tags: Go, Java, JavaScript, Python, Python3
> question: Count Special Quadruplets (count-special-quadruplets)
> url: https://leetcode.cn/problems/count-special-quadruplets/solutions/4iAc7p/pythonjavajavascriptgo-liang-shu-zhi-he-optkq/

---
### 解题思路
和LC经典的第一题有异曲同工之处。枚举左边两者和，枚举右边两者差，动态更新相同数目到答案。

另外同样可以采用背包动态规划思想，我们要选三个到背包里，维护 不选的各个值的个数、选一个各个值的个数、选两个各个值的个数、选三个各个值的个数。
在遍历到每个数，统计选三个了的各值中该数的个数就是答案的一部分。

### 代码

```Python3 []
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        l, ans = Counter(), 0
        for i in range(1, len(nums) - 2):
            # 到目前为止统计了所有0到i的两坐标和
            for j in range(i):
                l[nums[i] + nums[j]] += 1
            # 目前第三个坐标为i+1，枚举第四个坐标j的范围
            for j in range(i + 2, len(nums)):
                # 叠加以前统计的左半段和的结果，i+1作为第三个idx和j最多组成这么多
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

### 复杂度

时间复杂度 $o(n^{2})$