# [Python/Java/JavaScript/Go] 哈希统计模拟

> Author: Benhao
> Date: 2022-02-06
> Upvotes: 10
> Tags: Go, Java, JavaScript, Python, Python3

---

```Python3 []
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k,v in Counter(nums).items() if v == 1)
```
```Java []
class Solution {
    public int sumOfUnique(int[] nums) {
        Set<Integer> first = new HashSet<>(), second = new HashSet<>();
        int ans = 0;
        for(int num: nums)
            if(!first.contains(num)) {
                ans += num;
                first.add(num);
            } else if(!second.contains(num)) {
                ans -= num;
                second.add(num);
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
var sumOfUnique = function(nums) {
    const cnts = new Array(101).fill(0)
    let ans = 0
    for(const num of nums)
        if(cnts[num] == 0) {
            ans += num
            cnts[num]++
        } else if(cnts[num] == 1) {
            ans -= num
            cnts[num]++
        }
    return ans
};
```
```Go []
func sumOfUnique(nums []int) (ans int) {
    cnts := make([]int, 101)
    for _, num := range nums {
        if cnts[num] == 0 {
            ans += num
        } else if cnts[num] == 1 {
            ans -= num
        }
        cnts[num]++
    }
    return
}
```