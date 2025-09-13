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

## 线性基求最大异或子集

```python
def find_maximum_xor(arr):
    if not arr:
        return 0
    base = [0] * 32
    
    for x in arr:
        for i in range(31, -1, -1):
            if (x >> i) & 1:
                if base[i]:
                    x ^= base[i]
                else:
                    base[i] = x
                    break
    
    res = 0
    for i in range(31, -1, -1):
        if base[i] != 0 and (res >> i) & 1 == 0:
            res ^= base[i]
            
    return res
```