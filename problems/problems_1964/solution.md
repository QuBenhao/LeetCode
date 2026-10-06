# [Python/Java] Longest nondecreasing subsequence

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 2
> Tags: Java, Python, Python3

---

### Approach
Use the same idea as LIS, optimized to O(nlogn) with binary search.

Maintain the tail values of the current longest nondecreasing subsequences. Find the current element's insertion position, using bisect_right so equal values go to the right. Its longest length is insertion index + 1, covering positions 0 through idx.

### Code

```Python3 []
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        stack = []
        for num in obstacles:
            if not stack or stack[-1] <= num:
                stack.append(num)
                ans.append(len(stack))
            else:
                idx = bisect.bisect_right(stack, num)
                stack[idx] = num
                ans.append(idx + 1)
        return ans
```
```Java []
class Solution {
    List<Integer> stack;
    int[] ans;
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        int n = obstacles.length;
        ans = new int[n];
        stack = new ArrayList<>();
        for(int i=0;i<n;i++){
            if(stack.size() == 0 || stack.get(stack.size()-1) <= obstacles[i]){
                stack.add(obstacles[i]);
                ans[i] = stack.size();
            }
            else{
                int idx = binarySearch(obstacles[i]);
                stack.set(idx, obstacles[i]);
                ans[i] = ++idx;
            }
        }
        return ans;
    }

    public int binarySearch(int target){
        int l = 0, r = stack.size() - 1;
        while(l < r){
            int mid = (l + r) >> 1;
            if(stack.get(mid) <= target)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
}
```
