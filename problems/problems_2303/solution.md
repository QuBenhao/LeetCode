# [C] 模拟

> slug: c-mo-ni-by-himymben-p8if
> date: 2023-01-23
> tags: C, Go, Java, Python3, TypeScript
> question: Calculate Amount Paid in Taxes (calculate-amount-paid-in-taxes)
> url: https://leetcode.cn/problems/calculate-amount-paid-in-taxes/solutions/JGCmw0/c-mo-ni-by-himymben-p8if/

---
```C []
double calculateTax(int** brackets, int bracketsSize, int* bracketsColSize, int income){
    int i, ans = 0, pre = 0;
    for (i = 0; i < bracketsSize; i++) {
        if (income <= brackets[i][0]) {
            ans += (income - pre) * brackets[i][1];
            break;
        } else {
            ans += (brackets[i][0] - pre) * brackets[i][1];
        }
        pre = brackets[i][0];
    }
    return ans / 100.0;
}
```