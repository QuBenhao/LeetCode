# [Python/Java] Greedy with a max heap

> slug: pythonjava-da-ding-dui-tan-xin-by-himymb-ms90
> date: 2021-09-07
> tags: Java, Python, Python3
> question: IPO (ipo)
> url: https://leetcode.cn/problems/ipo/solutions/2OvHdW/pythonjava-da-ding-dui-tan-xin-by-himymb-ms90/

---
### Approach
We need to know `which project has the highest profit among those whose required capital does not exceed our current capital`. Pair the inputs and sort them by required capital. During each iteration, add every affordable project to a max heap that tracks the available profits, then choose the most profitable project. If our current capital cannot fund any remaining project, it can no longer increase, so stop.

Note: Always choose the most profitable project because the number of projects we can take is limited. Larger profits lead to a larger final result.

### Code

```Python3 []
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # Pair profits with capital and sort by required capital so every affordable project can be selected
        projects = sorted(zip(profits, capital), key=lambda x:x[1])
        cur = []
        idx = 0
        while k:
            # Add every project whose required capital does not exceed our current capital to the max heap
            while idx < n and projects[idx][1] <= w:
                heapq.heappush(cur, -projects[idx][0])
                idx += 1
            # If the max heap contains any projects, take the most profitable one.
            if cur:
                w -= heapq.heappop(cur)
            else:
                break
            k -= 1
        return w
```
```Java []
class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        int[][] projects = new int[n][2];
        for(int i=0;i<n;i++){
            projects[i][0] = capital[i];
            projects[i][1] = profits[i];
        }
        Arrays.sort(projects, (a, b)->a[0] - b[0]);
        PriorityQueue<Integer> cur = new PriorityQueue<>((a,b)->b-a);
        for(int i=0,idx=0;i < k; i++){
            while(idx < n && projects[idx][0] <= w)
                cur.add(projects[idx++][1]);
            if(cur.size() > 0)
                w += cur.poll();
            else
                break;
        }
        return w;
    }
}
```
