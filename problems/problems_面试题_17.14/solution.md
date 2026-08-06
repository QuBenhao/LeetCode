# [Python/Java] 大顶堆

> slug: pythonjava-da-ding-dui-by-himymben-za2u
> date: 2021-09-02
> tags: Python, Python3
> question: Smallest K LCCI (smallest-k-lcci)
> url: https://leetcode.cn/problems/smallest-k-lcci/solutions/2bxjRU/pythonjava-da-ding-dui-by-himymben-za2u/

---
### 解题思路
我们需要k个最小数，记录一个大小为k的大顶堆即可，每次超过长度就退出最大的元素(所以用大顶堆)。
同理需要k个最大数，记录大小为k的小顶堆即可。

### 代码

```Python3 []
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        ans = []
        for num in arr:
            heapq.heappush(ans, -num)
            if len(ans) > k:
                heapq.heappop(ans)
        return [-num for num in ans]
```
```Java []
class Solution {
    public int[] smallestK(int[] arr, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>((a,b)->b-a);
        for(int num:arr){
            queue.add(num);
            if(queue.size()>k)
                queue.poll();
        }
        int[] ans = new int[k];
        for(int i=0;i<k;i++)
            ans[i] = queue.poll();
        return ans;
    }
}
```