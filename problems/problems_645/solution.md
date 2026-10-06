# [Python] Three approaches

> Author: Benhao
> Date: 2021-07-03
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
The first approach looks fancy, but the idea is simple and relatively slow. The repeated number is the only one occurring twice, so use most_common(1). The missing number is the set of all expected numbers minus the set of present numbers.
<br>
The second approach uses arithmetic. The expected sum from 1 to n is (n+1)*n//2, the actual sum is sum(nums), and the sum after deduplication is sum(set(nums)). Actual minus deduplicated gives the repeated number; expected minus deduplicated gives the missing number.
<br>
The third approach uses bitwise operations and the least space. XOR the numbers from 1 to n, then XOR all of nums. XORing these two results gives the XOR of the repeated and missing numbers. I used the negative-marking technique from [this code](https://leetcode.com/problems/set-mismatch/discuss/105513/XOR-one-pass) to find the repeated number.

### Code

```python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Repeated number on the left, missing number on the right
        return [Counter(nums).most_common(1)[0][0], (set(i for i in range(1, len(nums) + 1)) - set(nums)).pop()]

```

```python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # # Repeated number on the left, missing number on the right
        # x = sum(nums) - sum(set(nums))
        # sum(nums) = x + 1 + ... + n - y
        # y = x + 1 + ... + n - sum(nums) = x + n * (n+1)//2 - sum(nums) = n * (n+1) // 2 - sum(set(nums))
        n, s = len(nums), sum(set(nums))
        return [sum(nums) - s, n * (n + 1) // 2 - s]
```

```python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 1 ^ 2 ^ ... ^ 4k = 4k
        # 1 ^ 2 ^ ... ^ 4k+1 = 4k ^ 4k+1 = 1
        # 1 ^ 2 ^ ... ^ 4k+2 = 4k+2 ^ 1 = 4k+3
        # 1 ^ 2 ^ ... ^ 4k+3 = 0
        n = len(nums)
        # Expected XOR result
        ans = [n, 1, n+1, 0][n%4]
        # Actual XOR result and the repeated number
        res = repeat = 0
        for num in nums:
            val = abs(num)
            res ^= val
            if nums[val-1] < 0:
                repeat = val
            else:
                nums[val-1] = -nums[val-1]
        # res omits one XOR with the missing number and adds one with the repeated number, so res^ans=x^y
        return [repeat, repeat ^ res ^ ans]
```
