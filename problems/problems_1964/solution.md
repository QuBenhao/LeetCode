# [Python/Java] 最长非递减子序列

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 2
> Tags: Java, Python, Python3

---

### 解题思路
和LIS思路差不多，用二分优化到O(nlogn)

维护一个当前的最长非递减子序列的栈，找当前元素的插入位置（相等插入位置要往右，所以用bisect_right!），那么它的最长长度就是它插入的下标+1(从0到idx构成的序列)

### 代码

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