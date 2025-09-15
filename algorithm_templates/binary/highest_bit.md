# 位运算——取最高位

```c++
int highBit(unsigned int n) {
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    return 31 - __builtin_clz((n + 1) >> 1);
}
```

```golang
31 - bits.LeadingZeros32(uint32(n))
```

```java
31 - Integer.numberOfLeadingZeros(k - 1);
```