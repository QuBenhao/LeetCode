# [Python/Java] Find the maximum transfer count

> slug: pythonjava-zhao-zui-da-chuan-shu-liang-b-cj8f
> date: 2021-09-28
> tags: Java, Python, Python3
> question: Super Washing Machines (super-washing-machines)
> url: https://leetcode.cn/problems/super-washing-machines/solutions/VLlaZl/pythonjava-zhao-zui-da-chuan-shu-liang-b-cj8f/

---
### Approach
Several washing machines can send clothes at the same time, so find the machine that needs the most transfers.
A machine that sends clothes in both directions needs the counts added together, so handle that case separately.

### Code

```Python3 []
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n:
            return -1
        avg = total // n
        ans = cur = 0
        for m in machines:
            # The case where clothes must be sent in both directions
            if cur < 0 and cur + m - avg > 0:
                # Add the counts: cur transfers to the left and cur+m-avg transfers to the right
                # ans = max(ans, abs(cur) + abs(cur + m - avg))
                # Under the condition above, this expression simplifies to
                ans = max(ans, m - avg)
                cur += m - avg
            else:
                # The cumulative difference so far
                cur += m - avg
                # The maximum number of transfers needed to borrow/send clothes from left to right
                ans = max(ans, abs(cur))
        return ans
```
```Java []
class Solution {
    public int findMinMoves(int[] machines) {
        int sum = 0, n = machines.length;
        for(int m:machines)
            sum += m;
        if(sum % n != 0)
            return -1;
        int ans = 0, cur = 0;
        int avg = sum / n;
        for(int m: machines){
            int diff = m - avg;
            if(cur < 0 && cur + diff > 0){
                ans = Math.max(ans, diff);
                cur += diff;
            } else{
                cur += diff;
                ans = Math.max(ans, Math.abs(cur));
            }
        }
        return ans;
    }
}
```
