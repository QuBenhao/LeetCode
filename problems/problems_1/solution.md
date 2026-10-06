# [Python/Java/JavaScript/Go] Two Sum

> Author: Benhao
> Date: 2022-03-23
> Upvotes: 14
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Use a hash table to record the indices of previously visited numbers. Check whether the difference between the target and the current value has appeared before; if so, the two numbers sum to the target.

### Code

```Python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = dict()
        for i, num in enumerate(nums):
            if (d := target - num) in idx_map:
                return [idx_map[d], i]
            idx_map[num] = i
```
```Java []
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int d = target - nums[i];
            if(map.containsKey(d)) {
                return new int[]{map.get(d), i};
            }
            map.put(nums[i], i);
        }
        return null;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map()
    for(let i = 0; i < nums.length; i++) {
        const d = target - nums[i]
        if(map.has(d)) {
            return [map.get(d), i]
        }
        map.set(nums[i], i)
    }
};
```
```Go []
func twoSum(nums []int, target int) (ans []int) {
    idxMap := map[int]int{}
    for i, num := range nums {
        if v, ok := idxMap[target - num]; ok {
            ans = []int{v, i}
            break
        }
        idxMap[num] = i
    }
    return
}
```
