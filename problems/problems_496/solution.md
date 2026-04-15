# [Python/Java/JavaScript] 单调栈

> Author: Benhao
> Date: 2021-10-25
> Upvotes: 18
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
使用单调栈+哈希表扫描`nums2`，得到并记录每个数字(题目说了互不相同)对应的比它最近的大数是哪个。

在单调栈中，只有比栈顶元素小的元素才能入栈，而这就相当于扫描到现在还没有出现比栈顶元素大(栈是单调的，里面都比栈顶大)的数。一旦出现了比栈顶大的，我们要一直弹出数，所有比它小的数都已经找到了需要的数(也就是它了)，直到并不再比它小，一直记录到最后。

### 代码

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