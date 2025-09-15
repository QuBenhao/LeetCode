# 数位dp

数位DP用于解决数字各位相关的计数问题，例如统计区间内满足特定条件的数字数量。其核心是通过动态规划逐位处理数字，利用记忆化技术避免重复计算。

## **核心思想**

1. **拆解数位**：将数字转换为字符数组，逐位处理。
2. **状态记录**：记录当前位置、是否受上界限制、前导零状态及其他条件。
3. **记忆化搜索**：缓存已计算的状态，优化时间复杂度。

## **通用步骤**

1. **预处理数位**：将数字转换为字符串或数组。
2. **递归处理每一位**：
    - **限制条件**：当前位是否受上界限制。
    - **前导零处理**：标记是否处于前导零状态。
    - **状态转移**：根据当前位选择更新状态。
3. **边界处理**：处理完所有位后返回结果。

## **Python 模板（以统计无重复数字为例）**

```python
from functools import lru_cache


def count_special_numbers(n: int) -> int:
    s = str(n)

    @lru_cache(maxsize=None)
    def dp(pos: int, mask: int, tight: bool, lead: bool) -> int:
        if pos == len(s):
            return 0 if lead else 1

        limit = int(s[pos]) if tight else 9
        total = 0

        for d in range(0, limit + 1):
            new_tight = tight and (d == limit)
            new_lead = lead and (d == 0)

            if new_lead:
                total += dp(pos + 1, mask, new_tight, new_lead)
            else:
                if (mask & (1 << d)) == 0:
                    new_mask = mask | (1 << d)
                    total += dp(pos + 1, new_mask, new_tight, new_lead)

        return total

    return dp(0, 0, True, True)


# 示例：统计1到n中无重复数字的数目
print(count_special_numbers(20))  # 输出19（1-20中除11外都符合）
```

```go
package main

import (
	"fmt"
	"strconv"
)

func countSpecialNumbers(n int) int {
    s := strconv.Itoa(n)
    m := len(s)
    memo := make([][1 << 10]int, m)
    for i := range memo {
        for j := range memo[i] {
            memo[i][j] = -1 // -1 表示没有计算过
        }
    }
    var dfs func(int, int, bool, bool) int
    dfs = func(i, mask int, isLimit, isNum bool) (res int) {
        if i == m {
            if isNum {
                return 1 // 得到了一个合法数字
            }
            return
        }
        if !isLimit && isNum {
            p := &memo[i][mask]
            if *p >= 0 { // 之前计算过
                return *p
            }
            defer func() { *p = res }() // 记忆化
        }
        if !isNum { // 可以跳过当前数位
            res += dfs(i+1, mask, false, false)
        }
        d := 0
        if !isNum {
            d = 1 // 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
        }
        up := 9
        if isLimit {
            up = int(s[i] - '0') // 如果前面填的数字都和 n 的一样，那么这一位至多填数字 s[i]（否则就超过 n 啦）
        }
        for ; d <= up; d++ { // 枚举要填入的数字 d
            if mask>>d&1 == 0 { // d 不在 mask 中，说明之前没有填过 d
                res += dfs(i+1, mask|1<<d, isLimit && d == up, true)
            }
        }
        return
    }
    return dfs(0, 0, true, false)
}
```

## **关键参数解释**

| 参数      | 说明                                  |
|---------|-------------------------------------|
| `pos`   | 当前处理的数位位置（从高位到低位）。                  |
| `mask`  | 状态掩码，记录已使用的数字（例如用位掩码表示）。            |
| `tight` | 是否受上界限制（如处理到第`i`位时，前`i-1`位是否与上界相同）。 |
| `lead`  | 是否处于前导零状态（前导零不计入已使用数字）。             |

## **适用场景**

1. **无重复数字计数**：如示例所示。
2. **数位和限制**：统计数位和等于特定值的数字。
3. **特定模式匹配**：如包含/不包含某些子序列。

通过合理设计状态转移和记忆化策略，数位DP能高效解决复杂的数位计数问题。模板可根据具体问题调整状态定义和转移逻辑。

## 模板 2.0

```python
from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = list(map(int, str(finish)))  # 避免在 dfs 中频繁调用 int()
        n = len(high)
        low = list(map(int, str(start).zfill(n)))  # 补前导零，和 high 对齐
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff:  # 枚举这个数位填什么
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:  # 这个数位只能填 s[i-diff]
                x = int(s[i - diff])
                if lo <= x <= hi:  # 题目保证 x <= limit，无需判断
                    res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res

        return dfs(0, True, True)
```

```go
package main

func numberOfPowerfulInt(start, finish int64, limit int, s string) int64 {
	low := strconv.FormatInt(start, 10)
	high := strconv.FormatInt(finish, 10)
	n := len(high)
	low = strings.Repeat("0", n-len(low)) + low // 补前导零，和 high 对齐
	diff := n - len(s)

	memo := make([]int64, n)
	for i := range memo {
		memo[i] = -1
	}
	var dfs func(int, bool, bool) int64
	dfs = func(i int, limitLow, limitHigh bool) (res int64) {
		if i == n {
			return 1
		}
		
		if !limitLow && !limitHigh {
			p := &memo[i]
			if *p >= 0 {
				return *p
			}
			defer func() { *p = res }()
		}

		// 第 i 个数位可以从 lo 枚举到 hi
		// 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
		lo := 0
		if limitLow {
			lo = int(low[i] - '0')
		}
		hi := 9
		if limitHigh {
			hi = int(high[i] - '0')
		}

		if i < diff { // 枚举这个数位填什么
			for d := lo; d <= min(hi, limit); d++ {
				res += dfs(i+1, limitLow && d == lo, limitHigh && d == hi)
			}
		} else { // 这个数位只能填 s[i-diff]
			x := int(s[i-diff] - '0')
			if lo <= x && x <= hi { // 题目保证 x <= limit，无需判断
				res += dfs(i+1, limitLow && x == lo, limitHigh && x == hi)
			}
		}
		return
	}
	return dfs(0, true, true)
}
```