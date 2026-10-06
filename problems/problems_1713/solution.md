# [Python/Java] Longest increasing subsequence

> Author: Benhao
> Date: 2021-07-26
> Upvotes: 29
> Tags: Java, Python, Python3

---

### Approach
Minimizing operations is equivalent to finding the longest common subsequence, since it requires the fewest insertions.
All values in target are distinct, so each value maps to a unique index.
Replace values in arr with their indices in target. The longest common subsequence then becomes the longest increasing subsequence of these indices.

This works because:
**A common subsequence always runs from left to right in target, so its indices must increase.**

### Code
```python3 []
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # Analysis:
        # Minimize operations by finding the longest common subsequence
        # Distinct values in target give every value a unique index
        # Map arr to indices in target; the longest common subsequence becomes a longest increasing subsequence

        # Map values to indices
        idx_dict = {num: i for i, num in enumerate(target)}
        # 300. Longest Increasing Subsequence
        stack = []
        for num in arr:
            # Only values present in target can belong to the common subsequence
            if num in idx_dict:
                # Convert to an index
                idx = idx_dict[num]
                # Position of this index in the current stack
                i = bisect.bisect_left(stack, idx)
                # Append if at the end; otherwise replace the element at this position
                # More generally, i is the sorted position of idx in stack
                # Earlier elements in stack larger than idx cannot precede idx in an increasing subsequence
                # Values left of i are smaller than idx and can precede it in an increasing subsequence of length i+1
                # Replacing stack[i] with the smaller idx leaves more room for later values to extend a subsequence
                if i == len(stack):
                    stack.append(0)
                stack[i] = idx
        # The final stack length is the LIS length; subtract it to obtain the answer
        return len(target) - len(stack)
```
```java []
class Solution {
    public int minOperations(int[] target, int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<target.length;i++)
            map.put(target[i], i);
        ArrayList<Integer> stack = new ArrayList<>();
        for(int num:arr){
            Integer idx = map.get(num);
            if(idx != null){
                int l=0,r=stack.size();
                while(l<r){
                    int mid = l + r >> 1;
                    if(stack.get(mid) >= idx)
                        r = mid;
                    else
                        l = mid + 1;
                }
                if(l == stack.size())
                    stack.add(idx);
                else
                    stack.set(l, idx);
            }
        } 
        return target.length - stack.size();
    }
}
```
