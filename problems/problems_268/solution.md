# [Python/Java/JavaScript/Go] 求和 或 异或

> slug: pythonjavajavascriptgo-qiu-he-deng-chai-z9kdy
> date: 2021-11-05
> tags: Go, Java, JavaScript, Python, Python3
> question: Missing Number (missing-number)
> url: https://leetcode.cn/problems/missing-number/solutions/8U6UKp/pythonjavajavascriptgo-qiu-he-deng-chai-z9kdy/

---
`求和`
```Python3 []
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (n:=len(nums)) * (n + 1) // 2 - sum(nums)
```
```Go []
func missingNumber(nums []int) int {
    n, sum := len(nums), 0
    for _, num := range nums{
        sum += num
    }
    return (n + 1) * n / 2 - sum
}
```

`如果求和怕溢出，用减法做`
```Go
func missingNumber(nums []int) int {
    ans := 0
    for i, num := range nums {
        ans += i + 1 - num
    }
    return ans
}
```

`异或性质`
```Python3 []
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums) ^ [(n:=len(nums)), 1, n + 1, 0][n%4]
```
```Java []
class Solution {
    public int missingNumber(int[] nums) {
        /**
         连续数字从1到n的异或规律 4 * k -> 4 * k
                4 * k + 1 -> 1
                4 * k + 2 -> 4 * k + 3
                4 * k + 3 -> 0
        */
        int n = nums.length, ans = 0;
        for(int num:nums)
            ans ^= num;
        switch(n % 4){
            case 1:
                return ans ^ 1;
            case 2:
                return (n + 1) ^ ans;
            case 3:
                return ans;
            default:
                return n ^ ans;
        }
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const n = nums.length;
    let ans = 0;
    for(const num of nums)
        ans ^= num;
    switch(n % 4){
        case 0:
            return ans ^ n;
        case 1:
            return ans ^ 1;
        case 2:
            return ans ^ (n + 1);
        default:
            return ans;
    }
};
```
```Go []
func missingNumber(nums []int) int {
    n, ans := len(nums), 0
    for _, num := range(nums) {
        ans ^= num
    }
    /**
    连续数字从1到n的异或规律 
    4 * k -> 4 * k
    4 * k + 1 -> 1
    4 * k + 2 -> 4 * k + 3
    4 * k + 3 -> 0
    */
    if v := n % 4; v == 0 {
        return n ^ ans
    } else if v == 1 {
        return v ^ ans
    } else if v == 2 {
        return (n + 1) ^ ans
    }
    return ans
}
```
```Go []
func missingNumber(nums []int) int {
    n, ans := len(nums), 0
    for _, num := range(nums) {
        ans ^= num
    }
    /**
    连续数字从1到n的异或规律 
    4 * k -> 4 * k
    4 * k + 1 -> 1
    4 * k + 2 -> 4 * k + 3
    4 * k + 3 -> 0
    */
    switch v := n % 4; v {
        case 0:
            return n ^ ans
        case 1:
            return v ^ ans
        case 2:
            return (n + 1) ^ ans
        default:
            return ans
    }
}
```