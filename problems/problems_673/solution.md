# [Python/Java] Count increasing subsequences by length and ending value

> slug: pythonjava-ji-lu-zui-chang-di-zeng-zi-xu-53ht
> date: 2021-09-20
> tags: Java, Python, Python3
> question: Number of Longest Increasing Subsequence (number-of-longest-increasing-subsequence)
> url: https://leetcode.cn/problems/number-of-longest-increasing-subsequence/solutions/HM1Ll7/pythonjava-ji-lu-zui-chang-di-zeng-zi-xu-53ht/

---
### Approach
When finding the longest increasing subsequence, maintain an array of tails, binary search for the current number's position, and use that position to determine its subsequence length. Here we also need counts. Once the length is known, sum the counts of all subsequences that can be extended by this number: those of `length-1` ending in a smaller number.

I spent a while trying to optimize this without success, then simply summed the counts at the previous length whose ending values are smaller than the current number.

### Code

```Python3 []
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Track the ending value, subsequence length, and count
        # 1 2 2 6 3 4 7
        dp = []
        # Map each length to counts for its different ending values
        records = defaultdict(list)
        # Initialize the empty subsequence count to 1
        records[0] = [(-inf, 1)]
        for num in nums:
            idx = bisect_left(dp, num)
            if idx < len(dp):
                dp[idx] = num
            else:
                dp.append(num)
            # idx + 1 is the longest increasing subsequence length ending here; its count comes from length-idx subsequences ending in smaller values
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
