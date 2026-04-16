# [C] 滑窗

> Author: Benhao
> Date: 2023-01-07
> Upvotes: 8
> Tags: C, Go, Java, Python3, TypeScript

---

题目可以转换为找一段最长的连续子数组，使得他们的和为sum(nums) - x

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