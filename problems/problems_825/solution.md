# [Python/Java/JavaScript/Go] 逻辑推导 + 前缀和统计

> Author: Benhao
> Date: 2021-12-26
> Upvotes: 38
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
```python3
# 根据题目我们知道加好友的条件需要满足如下布尔表达式：
# ! ( (ages[y] <= 0.5 * ages[x] + 7) || (ages[y] > ages[x]) || (ages[y] > 100 && ages[x] < 100) )
# 化简可得：
# ages[y] > 0.5 * ages[x] + 7 && ages[y] <= ages[x] && (ages[y] <= 100 || ages[x] >= 100)
# 也就是x和y满足以下两者之一，x就可以向y发送好友请求：
# 1. ages[y] <= ages[x] < (ages[y] - 7) * 2 && ages[y] <= 100
# 2. 0.5 * ages[x] + 7 < ages[y] <= ages[x] && ages[x] >= 100
```
我们使用第二个表达式即可，因为ages[x]小于100时，ages[y]小于等于ages[x]必然就满足ages[y] <= 100，所以只要满足另一半布尔表达式的要求。
根据这个布尔表达式我们知道，x可以添加好友的y是一个范围，可以使用前缀和快速统计一个范围内的人数，从而求解答案。

### 代码

```python3 []
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnts = [0] * (max(ages) + 1)
        for age in ages:
            cnts[age] += 1
        presum = [0] + list(accumulate(cnts))
        return sum(cnts[age] * max(0, presum[age + 1] - presum[age//2 + 8] - 1) for age in set(ages))
```
```Java []
class Solution {
    public int numFriendRequests(int[] ages) {
        int[] cnts = new int[120], presum = new int[121];
        for(int age: ages)
            cnts[age - 1]++;
        for(int i=1;i<121;i++)
            presum[i] = presum[i-1] + cnts[i-1];
        int ans = 0;
        for(int age: ages)
            ans += Math.max(0, presum[age] - presum[age/2 + 7] - 1);
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} ages
 * @return {number}
 */
var numFriendRequests = function(ages) {
    const cnts = new Array(120), presum = new Array(121)
    cnts.fill(0)
    presum.fill(0)
    for(const age of ages)
        cnts[age-1]++
    for(let i=1;i<121;i++)
        presum[i] = presum[i-1] + cnts[i-1]
    let ans = 0
    for(const age of ages)
        ans += Math.max(0, presum[age] - presum[Math.floor(age/2) + 7] - 1)
    return ans
};
```
```Go []
func numFriendRequests(ages []int) (ans int) {
    cnts, presum := make([]int, 120), make([]int, 121)
    for _, age := range ages {
        cnts[age - 1]++
    }
    for i:=1;i<121;i++{
        presum[i] = presum[i-1] + cnts[i-1];
    }
    for _, age := range ages{
        if v := presum[age] - presum[age/2+7] - 1; v > 0{
            ans += v
        }
    }
    return
}
```