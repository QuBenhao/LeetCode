# [Python] Dynamic programming with a rolling dictionary [comments added to reference code]

> slug: python-gun-dong-geng-xin-zi-dian-de-dong-xyfw
> date: 2021-05-11
> tags: Python, Python3
> question: 最多牌组数 (Up5XYM)
> url: https://leetcode.cn/problems/Up5XYM/solutions/Xo4zhs/python-gun-dong-geng-xin-zi-dian-de-dong-xyfw/

---
### Approach
After sorting, iterate through the values in tiles and roll the DP states forward to maximize the group count for each run-usage state.
See the comments for details.

### Code

```python3
class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        tiles = Counter(tiles)
        nums = sorted(tiles)
        # Roll dp forward across iterations; it stores the counts of runs ending at last_num+1 and last_num+2 formed at last_num, the value before num
        dp = {(0, 0): 0}
        # Is the DP update for d correct when nums has a gap, or when num+2 is absent and num+1 is the largest value?
        # When num reaches the maximum value (or a gap), v1 must be 0, so no positive d1 participates in the final loop over d;
        # only d1=0 is valid, which also forces d=0. The new dp has a value only at (0,0): the best result from the previous allocation of d0;
        # this matches the logic: without num+1 in tiles, neither num-1,num,num+1 nor num,num+1,num+2 can form a run
        for num in nums:
            v0, v1 = tiles[num], tiles[num+1]
            new_dp = Counter()
            # Enumerate how num and num+1 are used in runs num-2,num-1,num and num-1,num,num+1
            for (d0, d1), c in dp.items():
                # Enumerate all existing usage counts of num and num+1
                t0, t1 = v0 - d0, v1 - d1
                for d in range(min(t0, t1, 2) + 1):
                    # num+1 becomes the next num; its usage is the previous d1 plus d used in newly formed runs
                    # Use d copies of num+2
                    k = (d1 + d, d)
                    # DP: the best result for usage state k is the existing group count plus new runs plus triplets formed from the remaining num tiles
                    # All ways to use num in runs have now been enumerated; the remaining num tiles must form triplets
                    # Usage of the current num: 
                    # Form d0-d1 runs of num-2,num-1,num,
                    # form d1 runs of num-1,num,num+1,
                    # and form d runs of num,num+1,num+2
                    new_dp[k] = max(new_dp[k], c + d + (t0 - d) // 3)
            dp = new_dp
        return max(dp.values())

```
