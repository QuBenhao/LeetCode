# 取最低位

```c++
int lowBit(int n) {
    return n & -n;  // 等价于 n & (n ^ (n - 1))
}
```