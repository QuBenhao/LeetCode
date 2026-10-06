# [Python/Java/JavaScript/Go] Logical derivation + prefix sum counting

> Author: Benhao
> Date: 2021-12-26
> Upvotes: 38
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
```python3
# The problem states that a friend request must satisfy the following boolean expression:
# ! ( (ages[y] <= 0.5 * ages[x] + 7) || (ages[y] > ages[x]) || (ages[y] > 100 && ages[x] < 100) )
# Simplifying gives:
# ages[y] > 0.5 * ages[x] + 7 && ages[y] <= ages[x] && (ages[y] <= 100 || ages[x] >= 100)
# In other words, x can send y a friend request if either of the following holds:
# 1. ages[y] <= ages[x] < (ages[y] - 7) * 2 && ages[y] <= 100
# 2. 0.5 * ages[x] + 7 < ages[y] <= ages[x] && ages[x] >= 100
```
The second expression alone suffices: when ages[x] is below 100, ages[y] <= ages[x] already implies ages[y] <= 100, so only the other half of the boolean expression needs to be checked.
This boolean expression shows that the eligible y values form a range. Prefix sums count the people in that range efficiently to compute the answer.

### Code

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
