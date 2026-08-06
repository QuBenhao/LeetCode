# [Python/Java/TypeScript/Go] 模拟 

> slug: p-by-himymben-r24t
> date: 2022-09-18
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Sort Array by Increasing Frequency (sort-array-by-increasing-frequency)
> url: https://leetcode.cn/problems/sort-array-by-increasing-frequency/solutions/PXN8OD/p-by-himymben-r24t/

---
### 解题思路
哈希表自定义排序

### 代码

```Python3 []
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:(mp[x], -x)) if (mp := Counter(nums)) else nums
```
```Java []
class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        return Arrays.stream(nums).boxed().sorted((a, b) -> {
            if (map.get(a) != map.get(b)) {
                return map.get(a) - map.get(b);
            }
            return b - a;
        }).mapToInt(Integer::valueOf).toArray();
    }
}
```
```TypeScript []
function frequencySort(nums: number[]): number[] {
    const mp: Map<number, number> = new Map<number, number>()
    for (const num of nums) {
        mp.set(num, (mp.get(num) || 0) + 1)
    }
    nums.sort((a, b) => {
        if (mp.get(a) != mp.get(b)) {
            return mp.get(a) - mp.get(b)
        }
        return b - a
    })
    return nums
};
```
```Go []
func frequencySort(nums []int) []int {
    mp := map[int]int{}
    for _, num := range nums {
        mp[num]++
    }
    sort.Slice(nums, func(i, j int) bool{
        if mp[nums[i]] != mp[nums[j]] {
            return mp[nums[i]] < mp[nums[j]]
        }
        return nums[i] > nums[j]
    })
    return nums
}
```