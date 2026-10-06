# [Python/Java/JavaScript/Go] Count frequencies or sort with two pointers

> Author: Benhao
> Date: 2021-11-19
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Count occurrences with a HashMap, then iterate over the values and check for neighboring values to calculate the answer from their counts.

Alternatively, count occurrences and update the maximum as you traverse.

Another approach is sorting with two pointers, which uses less space: count the current number, then the number one greater than it, and update the answer.

### Code
```Python3 
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        return max(v + cnts[k+1] if k + 1 in cnts else 0 for k,v in cnts.items())
```

```Python3 []
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = defaultdict(int)
        ans = 0
        for num in nums:
            cnts[num] += 1
            if num + 1 in cnts:
                ans = max(ans, cnts[num] + cnts[num + 1])
            if num - 1 in cnts:
                ans = max(ans, cnts[num] + cnts[num - 1])
        return ans
```
```Java []
class Solution {
    public int findLHS(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
            if(map.containsKey(num + 1))
                ans = Math.max(ans, map.get(num) + map.get(num+1));
            if(map.containsKey(num - 1))
                ans = Math.max(ans, map.get(num) + map.get(num-1));
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
var findLHS = function(nums) {
    const cnts = new Map();
    let ans = 0;
    for(const num of nums){
        if(cnts.has(num))
            cnts.set(num, cnts.get(num) + 1);
        else
            cnts.set(num, 1);
        if(cnts.has(num + 1))
            ans = Math.max(ans, cnts.get(num) + cnts.get(num + 1));
        if(cnts.has(num - 1))
            ans = Math.max(ans, cnts.get(num) + cnts.get(num - 1));        
    }
    return ans;
};
```
```Go []
func findLHS(nums []int) int {
    cnts := map[int]int{}
    ans := 0
    for _, num := range nums {
        cnts[num] = cnts[num] + 1
        if v := cnts[num + 1]; v > 0 {
            if v + cnts[num] > ans {
                ans = v + cnts[num]
            }
        }
        if v := cnts[num - 1]; v > 0 {
            if v + cnts[num] > ans {
                ans = v + cnts[num]
            }
        }
    }
    return ans
}

```
---
```Python3 []
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        ans = i = j = 0
        while i < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            nxt = j
            while j < len(nums) and nums[j] == nums[i] + 1:
                j += 1
            if j > nxt:
                ans = max(ans, j - i)
            i = nxt
        return ans
```
```Java []
class Solution {
    public int findLHS(int[] nums) {
        Arrays.sort(nums);
        int ans = 0, n = nums.length;
        for(int i=0, j=0;i<n;){
            while(j < n && nums[j] == nums[i])
                j++;
            int nxt = j;
            while(j < n && nums[j] == nums[i] + 1)
                j++;
            if(j > nxt)
                ans = Math.max(ans, j - i);
            i = nxt;
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
var findLHS = function(nums) {
    nums.sort(function(a,b){return a-b;});
    let ans = 0;
    const n = nums.length;
    for(let i=0, j=0;i<n;){
        while(j<n && nums[j] == nums[i])
            j++;
        const nxt = j;
        while(j<n && nums[j] == nums[i] + 1)
            j++;
        if(j > nxt)
            ans = Math.max(ans, j - i);
        i = nxt;
    }
    return ans;
};
```
```Go []
func findLHS(nums []int) int {
    sort.Ints(nums)
    ans, n, i, j := 0, len(nums), 0, 0
    for i < n {
        for j < n && nums[j] == nums[i] {
            j++
        }
        nxt := j
        for j < n && nums[j] == nums[i] + 1 {
            j++
        }
        if j > nxt && j - i > ans {
            ans = j - i
        }
        i = nxt
    }
    return ans
}
```
