# [Python/Java] Dynamic programming

> Author: Benhao
> Date: 2021-08-10
> Upvotes: 17
> Tags: Java, Python, Python3

---

### Approach
The code comments explain the reasoning; here is more detail. We must consider the difference between every pair to find all arithmetic subsequences, but brute-force searching for all matching differences is too slow. Instead, consider how to extend known prefixes. If we have [2,4], each later 6 forms a valid subsequence. After adding 6, there are two relevant differences: 2 for [2,4,6] and 4 for [2,6]. The first now needs an 8, and the second needs a 10.

For example, consider [2,4,6,8,10].
In the first round, start at 2. The differences to later values are [2,4,6,8], so each later value needs a following value in [4+2, 6+4, 8+6, 10+8] to extend an arithmetic subsequence.
In the second round, start at 4. The differences to later values are [2,4,6]. The first round already recorded a need for a value 2 greater than 4, so this difference extends an arithmetic subsequence. When 6 looks for another value at difference 2, add the previous count for 4 with difference 2. This ensures that 8 counts both [2,4,6,8] and [4,6,8], while 10 counts [2,4,6,8,10], [4,6,8,10], and [6,8,10].

> Why add the counts?
> Consider [2, 4, 2, 4, 6, 8].
> The 6 forms an arithmetic subsequence with each of three [2, 4] pairs.

### Code

```Python3 []
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # For three values to form an arithmetic subsequence, use the first two values' difference and look for the second value plus that difference later
        # For example, in [2, 4, 6, 6, 6], 2 and 4 form an answer with each of the three 6s
        # For a fixed prefix, track the required val and the number of preceding arithmetic subsequences corresponding to it
        
        n, ans = len(nums), 0
        dp = [Counter() for _ in range(n)]
        # Current final value of an arithmetic subsequence (possibly only this value so far)
        for i in range(n-1):
            # Can adding this value extend an arithmetic subsequence ending there?
            for j in range(i + 1, n):
                # Current difference, used to match arithmetic subsequences ending at i
                diff = nums[j] - nums[i]
                # If a subsequence ending there has difference diff, j extends it; add one more for the new pair [i,j]
                # Otherwise, j and i form an initial pair with count (0+1); a later value differing from j by diff can complete a subsequence
                dp[j][diff] += dp[i][diff] + 1
                # Combining i, j, and the preceding subsequences ending at i with difference diff gives this many new arithmetic subsequences
                # As in yesterday's problem, [i] and [j] produce a valid subsequence only when [i] already ends one with difference diff (at least two values, making at least three with j)
                ans += dp[i][diff]
        return ans
```
```Java []
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length, ans = 0;
        // Index 0 does not need a HashMap
        Map<Long, Integer>[] dp = new Map[n - 1];
        for(int i=1;i<n;i++)
            dp[i-1] = new HashMap<>();
        // Current endpoint of some arithmetic subsequences
        for(int i=0;i<n-1;i++)
            // Can the value being added extend any arithmetic subsequence ending here?
            for(int j=i+1;j<n;j++){
                // diff can be as large as 2^33 - 1, overflowing int, so use long
                long diff = 1L * nums[j] - nums[i];
                // Number of arithmetic subsequences currently ending at i with difference diff
                int cnts = i > 0 ? dp[i-1].getOrDefault(diff, 0) : 0;
                // Each such subsequence ending at i can combine with j to form a new arithmetic subsequence
                ans += cnts;
                // Number of new arithmetic subsequences ending at j with difference diff (i -> j)
                dp[j-1].put(diff, dp[j-1].getOrDefault(diff, 0) + cnts + 1);
            }
        return ans;
    }
}
```
