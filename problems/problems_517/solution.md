# [Python/Java] 找最大传输量

> slug: pythonjava-zhao-zui-da-chuan-shu-liang-b-cj8f
> date: 2021-09-28
> tags: Java, Python, Python3
> question: Super Washing Machines (super-washing-machines)
> url: https://leetcode.cn/problems/super-washing-machines/solutions/VLlaZl/pythonjava-zhao-zui-da-chuan-shu-liang-b-cj8f/

---
### 解题思路
由于一次可以多个洗衣机送衣服，所以我们只要找要送最多次的洗衣机即可。
由于一个洗衣机往两边都送的话，要叠加统计次数，所以特殊处理。

### 代码

```Python3 []
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n:
            return -1
        avg = total // n
        ans = cur = 0
        for m in machines:
            # 向两边都送的情况
            if cur < 0 and cur + m - avg > 0:
                # 我们既需要往左边送cur次，又需要往右边送cur+m-avg次，所以叠加
                # ans = max(ans, abs(cur) + abs(cur + m - avg))
                # 上面的式子根据判断条件就变成
                ans = max(ans, m - avg)
                cur += m - avg
            else:
                # 当前累计出的差值
                cur += m - avg
                # 从左到右最多需要借/送多少次
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