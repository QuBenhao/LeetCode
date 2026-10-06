# [Python/Java] Max-heap

> slug: pythonjava-da-ding-dui-by-himymben-za2u
> date: 2021-09-02
> tags: Python, Python3
> question: Smallest K LCCI (smallest-k-lcci)
> url: https://leetcode.cn/problems/smallest-k-lcci/solutions/2bxjRU/pythonjava-da-ding-dui-by-himymben-za2u/

---
### Approach
To find the k smallest numbers, maintain a max-heap of size k. Whenever it grows beyond k, remove the largest element; this is why a max-heap is used.
Likewise, use a min-heap of size k to find the k largest numbers.

### Code

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
