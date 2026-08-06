# [Python/Java] 记录最长递增子序列不长度不同末尾的个数

> slug: pythonjava-ji-lu-zui-chang-di-zeng-zi-xu-53ht
> date: 2021-09-20
> tags: Java, Python, Python3
> question: Number of Longest Increasing Subsequence (number-of-longest-increasing-subsequence)
> url: https://leetcode.cn/problems/number-of-longest-increasing-subsequence/solutions/HM1Ll7/pythonjava-ji-lu-zui-chang-di-zeng-zi-xu-53ht/

---
### 解题思路
在求最长公共子序列的时候，我们维护一个序列数组，二分查找当前数的位置，然后用这个位置计算该数的序列长度。但是这题我们需要额外统计个数，每次我们找到该数的最长递增子序列的长度后，需要求和该所有能构成以这个数结尾的个数，而这个正是`长度-1`中小于这个数的个数的和。

调了半天优化的…未遂…遂直接暴力统计上一个长度小于当前数的个数的叠加。

### 代码

```Python3 []
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #  我们需要知道的是 末尾数字大小以及其长度以及个数
        # 1 2 2 6 3 4 7
        dp = []
        # 长度 映射 不同的数字大小的个数
        records = defaultdict(list)
        # 初始化空的个数为1
        records[0] = [(-inf, 1)]
        for num in nums:
            idx = bisect_left(dp, num)
            if idx < len(dp):
                dp[idx] = num
            else:
                dp.append(num)
            # idx + 1 为 当前数字构成的最长递增子序列的长度，它的个数由 idx 长度中比它小的个数组成
            records[idx + 1].append((num, sum(v for k,v in records[idx] if k < num)))
        return sum(v[1] for v in records[max(records.keys())])
```
```Java []
class Solution {
    int INF = 0x3f3f3f;
    public int findNumberOfLIS(int[] nums) {
        List<Integer> dp = new ArrayList<>();
        Map<Integer, List<int[]>> records = new HashMap<>();
        records.put(0, new ArrayList(){{add(new int[]{-INF, 1});}});
        for(int num:nums){
            int idx = binarySearch(dp, num);
            if(idx < dp.size()){
                dp.set(idx, num);
            } else
                dp.add(num);
            int s = 0;
            for(int[] vals: records.get(idx)){
                if(vals[0] < num)
                    s += vals[1];
            }
            List<int[]> cur = records.getOrDefault(++idx, new ArrayList<>());
            cur.add(new int[]{num, s});
            records.put(idx, cur);
        }
        int m = 0;
        for(int k:records.keySet())
            m = Math.max(m, k);
        int ans = 0;
        for(int[] vals: records.get(m))
            ans += vals[1];
        return ans;
    }

    public int binarySearch(List<Integer> dp, int num){
        int l = 0, r = dp.size();
        while(l < r){
            int mid = l + (r - l) / 2;
            if(dp.get(mid) < num)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
}
```