# [C] 模拟

> slug: c-mo-ni-by-himymben-5ftv
> date: 2023-01-11
> tags: C, Go, Java, Python3, TypeScript
> question: Check if Number Has Equal Digit Count and Digit Value (check-if-number-has-equal-digit-count-and-digit-value)
> url: https://leetcode.cn/problems/check-if-number-has-equal-digit-count-and-digit-value/solutions/qGjrvf/c-mo-ni-by-himymben-5ftv/

---
```C []
bool digitCount(char * num){
    int i, n = strlen(num);
    int counts[n];
    for (i = 0; i < n; i++) {
        counts[i] = 0;
    }
    for (i = 0; i < n; i++) {
        int cur = num[i] - '0';
        if (cur >= n) {
            return false;
        }
        counts[cur]++;
    }
    for (i = 0; i < n; i++) {
        if (counts[i] != num[i] - '0') {
            return false;
        }
    }
    return true;
}
```
```Python3 []
```