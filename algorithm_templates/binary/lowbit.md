# Lowest set bit

```c++
int lowBit(int n) {
    return n & -n;  // Equivalent to n & (n ^ (n - 1))
}
```
