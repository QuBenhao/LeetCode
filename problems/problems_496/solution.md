# [Python/Java/JavaScript] Monotonic stack

> Author: Benhao
> Date: 2021-10-25
> Upvotes: 18
> Tags: Java, JavaScript, Python, Python3

---

### Approach
Scan `nums2` with a monotonic stack and hash table, recording each value's next greater value. The problem guarantees distinct values.

Only a value smaller than the top can be pushed without popping. Until a larger value appears, the stack's entries are still waiting for their next greater value, and all entries below the top are larger than it. When a larger value appears, keep popping smaller values and record this new value as their answer. Stop popping at a value that is not smaller, and continue to the end.

### Code

```Python3 []
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        window, d = [], dict()
        for num in nums2:
            while window and window[-1] < num:
                small = window.pop()
                d[small] = num
            window.append(num)
        return [d[num] if num in d else -1 for num in nums1]
```
```Java []
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Deque<Integer> stack = new ArrayDeque<Integer>();
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int num:nums2){
            while(stack.size() > 0  && stack.peek() < num){
                int small = stack.pop();
                map.put(small, num);
            }
            stack.push(num);
        }
        int[] ans = new int[nums1.length];
        for(int i=0;i<nums1.length;i++){
            if(map.containsKey(nums1[i]))
                ans[i] = map.get(nums1[i]);
            else
                ans[i] = -1;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    const stack = [], map = new Map();
    for(const num of nums2){
        while(stack.length > 0 && stack[stack.length - 1] < num){
            const small = stack.pop();
            map.set(small, num);
        }
        stack.push(num);
    }
    const ans = [];
    for(const num of nums1){
        if(map.has(num))
            ans.push(map.get(num));
        else
            ans.push(-1);
    }
    return ans;
};
```
