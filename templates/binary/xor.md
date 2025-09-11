# 异或

`xor`运算的性质：

1. $`a \oplus a = 0`$
2. $`a \oplus 0 = a`$
3. $`a \oplus b \oplus c = a \oplus c \oplus b`$

```python3
def single_number(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans
```

```go
package main

func singleNumber(nums []int) int {
    ans := 0
    for _, num := range nums {
        ans ^= num
    }
    return ans
}
```
