# [C] Sliding window

> Author: Benhao
> Date: 2023-01-07
> Upvotes: 8
> Tags: C, Go, Java, Python3, TypeScript

---

Reframe the problem as finding the longest contiguous subarray with sum sum(nums) - x.

```C []
int min(int a, int b) {
    if (a > b) {
        return b;
    }
    return a;
}

int minOperations(int* nums, int numsSize, int x){
    int i, sum = 0, ans = numsSize + 1;
    for (i = 0; i < numsSize; i++) {
        sum += nums[i];
    }
    sum -= x;
    i = 0;
    int j = 0, cur = 0;
    while (i < numsSize) {
        while (j < numsSize && cur < sum) {
            cur += nums[j++];
        }
        if (cur == sum) {
            ans = min(ans, numsSize + i - j);
        }
        cur -= nums[i++];
    }
    return ans <= numsSize ? ans : -1;
}
```
