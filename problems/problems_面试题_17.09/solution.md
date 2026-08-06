# [Python/Java/TypeScript/Go] K路归并

> slug: pythonjavatypescriptgo-klu-gui-bing-by-h-kxdf
> date: 2022-09-28
> tags: C++, Go, Java, JavaScript, Python, Python3, TypeScript
> question: Get Kth Magic Number LCCI (get-kth-magic-number-lcci)
> url: https://leetcode.cn/problems/get-kth-magic-number-lcci/solutions/J0ktc8/pythonjavatypescriptgo-klu-gui-bing-by-h-kxdf/

---
### 解题思路
归并应用裸题，每次取最小
[丑数题解](https://leetcode.cn/problems/ugly-number-ii/solution/gong-shui-san-xie-yi-ti-shuang-jie-you-x-3nvs/)

### 代码

最小堆
```python3
factors = [3, 5, 7]
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        ans, pq = 0, [1]
        while k:
            cur = heapq.heappop(pq)
            if ans < cur:
                ans = cur
                k -= 1
                for p in factors:
                    heapq.heappush(pq, p * cur)
        return ans
```
多路归并
```Python3 []
class Solution:
    def getKthMagicNumber(self, n: int) -> int:
        # ans 用作存储已有丑数（从下标 1 开始存储，第一个丑数为 1）
        ans = [0] * (n+1)
        ans[1] = 1
        # 由于三个有序序列都是由「已有丑数」*「质因数」而来
        # i2、i3 和 i5 分别代表三个有序序列当前使用到哪一位「已有丑数」下标（起始都指向 1）
        i2 = i3 = i5 = 1
        idx = 2
        while idx <= n:
            # 由 ans[iX] * X 可得当前有序序列指向哪一位
            a,b,c = ans[i2] * 3, ans[i3] * 5,ans[i5]* 7
            # 将三个有序序列中的最小一位存入「已有丑数」序列，并将其下标后移
            m = min(a,b,c)
            # 由于可能不同有序序列之间产生相同丑数，因此只要一样的丑数就跳过（不能使用 else if ）
            if m == a:
                i2 += 1
            if m == b:
                i3 += 1
            if m == c:
                i5 += 1
            ans[idx] = m
            idx += 1
        return ans[n]
```
```Java []
class Solution {
    public int getKthMagicNumber(int k) {
        int[] ans = new int[k + 1];
        ans[1] = 1;
        int idx = 2, i3 = 1, i5 = 1, i7 = 1;
        while (idx <= k) {
            int a = ans[i3] * 3, b = ans[i5] * 5, c = ans[i7] * 7;
            int m = Math.min(Math.min(a, b), c);
            if (m == a) {
                i3++;
            }
            if (m == b) {
                i5++;
            }
            if (m == c) {
                i7++;
            }
            ans[idx++] = m;
        }
        return ans[k];
    }
}
```
```TypeScript []
function getKthMagicNumber(k: number): number {
    const ans: Array<number> = new Array<number>(k + 1).fill(0)
    ans[1] = 1
    let idx: number = 2, i3: number = 1, i5: number = 1, i7: number = 1
    while (idx <= k) {
        const a: number = ans[i3] * 3, b: number = ans[i5] * 5, c: number = ans[i7] * 7
        const m: number = Math.min(a, b, c)
        if (m == a) {
            i3++
        }
        if (m == b) {
            i5++
        }
        if (m == c) {
            i7++
        }
        ans[idx++] = m
    }
    return ans[k]
};
```
```Go []
func getKthMagicNumber(k int) int {
    ans := make([]int, k + 1)
    ans[1] = 1
    for idx, i3, i5, i7 := 2, 1, 1, 1; idx <= k; idx++ {
        a, b, c := ans[i3] * 3, ans[i5] * 5, ans[i7] * 7
        m := min(a, b, c)
        if m == a {
            i3++
        }
        if m == b {
            i5++
        }
        if m == c {
            i7++
        }
        ans[idx] = m
    }
    return ans[k]
}

func min(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v < ans {
            ans = v
        }
    }
    return ans
}
```
```C++ []
class Solution {
public:
    int getKthMagicNumber(int k) {
        int ans[k + 1];
        ans[0] = 0; ans[1] = 1;
        for (int idx = 2, i3 = 1, i5 = 1, i7 = 1; idx <= k; idx++) {
            int a = ans[i3] * 3, b = ans[i5] * 5, c = ans[i7] * 7;
            int m = min(min(a, b), c);
            if (m == a) {
                i3++;
            }
            if (m == b) {
                i5++;
            }
            if (m == c) {
                i7++;
            }
            ans[idx] = m;
        }
        return ans[k];
    }
};
```