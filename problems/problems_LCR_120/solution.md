# [Python/Java/JavaScript/Go] 哈希 -> 坐标交换

> slug: pythonjavajavascriptgo-ha-xi-by-himymben-j25s
> date: 2021-11-25
> tags: Go, Java, JavaScript, Python, Python3
> question: 寻找文件副本 (shu-zu-zhong-zhong-fu-de-shu-zi-lcof)
> url: https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solutions/G1RSzX/pythonjavajavascriptgo-ha-xi-by-himymben-j25s/

---
```python3 []
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
```
```Java []
class Solution {
    public int findRepeatNumber(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for(int num:nums){
            if(s.contains(num))
                return num;
            s.add(num);
        }
        return 0;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
    const s = new Set()
    for(const num of nums){
        if(s.has(num))
            return num
        s.add(num)
    }
};
```
```Go []
func findRepeatNumber(nums []int) int {
    s := map[int]bool{}
    for _, num := range nums {
        if s[num] {
            return num
        }
        s[num] = true
    }
    return -1
}
```

既然数字都是0～n-1，可以看成是坐标并填入对应位置，填不了的时候就是重复的坐标（数字）了
```python3 []
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # 当前坐标与当前坐标的数不一致，交换到它该到的位置直到一致位置
            while nums[i] != i:
                num = nums[i]
                # 交换的位置已经填入自己了，说明重复了
                if nums[num] == num:
                    return num
                nums[num], nums[i] = nums[i], nums[num]
        return -1
```
```Java []
class Solution {
    public int findRepeatNumber(int[] nums) {
        for(int i=0;i<nums.length;i++){
            while(nums[i] != i){
                int num = nums[i];
                if(nums[num] == num)
                    return num;
                nums[i] = nums[num];
                nums[num] = num;
            }
        }
        return -1;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
    for(let i=0;i<nums.length;i++){
        while(nums[i] != i){
            const num = nums[i]
            if(nums[num] == num)
                return num
            nums[i] = nums[num]
            nums[num] = num
        }
    }
    return -1
};
```
```Go []
func findRepeatNumber(nums []int) int {
    for i := 0; i < len(nums); i++ {
        for nums[i] != i {
            if nums[nums[i]] == nums[i] {
                return nums[i]
            }
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        }
    }
    return -1
}
```
