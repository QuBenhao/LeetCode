# [Python/Java/JavaScript/Go] 两数之和

> Author: Benhao
> Date: 2022-03-23
> Upvotes: 14
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
使用哈希表记录之前遍历过的数字对应的坐标，检查当前值和目标值的差是否出现过，出现过意味着他们俩的和即为目标值。

### 代码

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