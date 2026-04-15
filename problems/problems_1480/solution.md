# [Python/Java] 前缀和裸题

> Author: Benhao
> Date: 2021-08-27
> Upvotes: 7
> Tags: Java, Python, Python3

---

```python3 []
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
```

```Java []

class Solution {
    public int[] runningSum(int[] nums) 	{
		int sum = 0, n = nums.length;
        int[] presum = new int[n];
        for(int i=0;i<n;i++){
			sum += nums[i];
            presum[i] = sum;
        }
        return presum;
    }
}

```