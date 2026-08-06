# [Python/Java] 大顶堆贪心

> slug: pythonjava-da-ding-dui-tan-xin-by-himymb-ms90
> date: 2021-09-07
> tags: Java, Python, Python3
> question: IPO (ipo)
> url: https://leetcode.cn/problems/ipo/solutions/2OvHdW/pythonjava-da-ding-dui-tan-xin-by-himymb-ms90/

---
### 解题思路
我们需要知道的信息是: `在需要的本金小于等于我们当前资本的项目中，利益最大的是哪个`，所以我们将输入组合起来并按本金排序，这样在循环中，所有小于等于当前本金的都可以加入到大顶堆中(维护所有可选的利益的堆)，于是我们就可以选到当前利益最大的那个的了。一种特殊情况是，如果我们当前的资本已经不支持任何项目了，也就是我们的钱再也不可能发生变化了，只能结束了。

注: 每次都选利益最大的那个是因为我们选项目的个数有限制，选的越大最终的答案才能越大。

### 代码

```Python3 []
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # 将profits和capital组合起来，并按本金排序，这样保证我们总能选取所有小于等于当前资本的
        projects = sorted(zip(profits, capital), key=lambda x:x[1])
        cur = []
        idx = 0
        while k:
            # 将所有需要的本金小于等于当前资本的项目加入最大堆
            while idx < n and projects[idx][1] <= w:
                heapq.heappush(cur, -projects[idx][0])
                idx += 1
            # 如果有项目在当前的大顶堆中，我们做利益最大的那一个。
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