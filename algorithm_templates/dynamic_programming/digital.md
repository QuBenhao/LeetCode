# Digit DP

Digit DP solves counting problems involving the digits of numbers, such as counting numbers in a range that satisfy a condition. It processes numbers digit by digit with dynamic programming and uses memoization to avoid repeated computation.

## **Core idea**

1. **Split the digits**: Convert the number to a character array and process one digit at a time.
2. **Track the state**: Record the current position, whether the upper bound applies, the leading-zero state, and any other conditions.
3. **Memoize the search**: Cache computed states to improve time complexity.

## **General steps**

1. **Prepare the digits**: Convert the number to a string or array.
2. **Process each digit recursively**:
    - **Bound constraint**: Track whether the current digit is constrained by the upper bound.
    - **Leading zeros**: Track whether the number is still in the leading-zero state.
    - **State transition**: Update the state based on the chosen digit.
3. **Base case**: Return the result after processing all digits.

## **Python template: counting numbers with distinct digits**

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


# Example: count numbers from 1 to n with distinct digits
print(count_special_numbers(20))  # Output: 19 (all numbers from 1 to 20 except 11 qualify)
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
            memo[i][j] = -1 // -1 means not yet computed
        }
    }
    var dfs func(int, int, bool, bool) int
    dfs = func(i, mask int, isLimit, isNum bool) (res int) {
        if i == m {
            if isNum {
                return 1 // Found a valid number
            }
            return
        }
        if !isLimit && isNum {
            p := &memo[i][mask]
            if *p >= 0 { // Already computed
                return *p
            }
            defer func() { *p = res }() // Memoization
        }
        if !isNum { // This digit position can be skipped
            res += dfs(i+1, mask, false, false)
        }
        d := 0
        if !isNum {
            d = 1 // If no digit has been placed yet, start at 1 to avoid leading zeros
        }
        up := 9
        if isLimit {
            up = int(s[i] - '0') // If all previous digits match n, this digit cannot exceed s[i], or the number would exceed n
        }
        for ; d <= up; d++ { // Try each digit d
            if mask>>d&1 == 0 { // d is absent from mask, so it has not been used
                res += dfs(i+1, mask|1<<d, isLimit && d == up, true)
            }
        }
        return
    }
    return dfs(0, 0, true, false)
}
```

## **Key parameters**

| Parameter | Description |
|---------|-------------------------------------|
| `pos`   | Current digit position, from most significant to least significant. |
| `mask`  | State mask recording the digits already used, for example as a bitmask. |
| `tight` | Whether the upper bound applies: at digit `i`, whether the preceding `i-1` digits match the bound. |
| `lead`  | Whether the number is still in the leading-zero state; leading zeros do not count as used digits. |

## **Use cases**

1. **Counting numbers with distinct digits**: As in the example above.
2. **Digit-sum constraints**: Count numbers whose digits sum to a specified value.
3. **Pattern matching**: For example, require or exclude certain subsequences.

With suitable state transitions and memoization, digit DP can efficiently solve complex digit-counting problems. Adapt the state definition and transition logic to the specific problem.

## Template 2.0

```python
from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = list(map(int, str(finish)))  # Avoid repeated int() calls in dfs
        n = len(high)
        low = list(map(int, str(start).zfill(n)))  # Pad with leading zeros to align with high
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # The digit at position i can range from lo to hi
            # Apply any additional digit constraints only in the for loop below; do not change lo or hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff:  # Try each choice for this digit
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:  # This digit must be s[i-diff]
                x = int(s[i - diff])
                if lo <= x <= hi:  # The problem guarantees x <= limit, so no check is needed
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
	low = strings.Repeat("0", n-len(low)) + low // Pad with leading zeros to align with high
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

		// The digit at position i can range from lo to hi
		// Apply any additional digit constraints only in the for loop below; do not change lo or hi
		lo := 0
		if limitLow {
			lo = int(low[i] - '0')
		}
		hi := 9
		if limitHigh {
			hi = int(high[i] - '0')
		}

		if i < diff { // Try each choice for this digit
			for d := lo; d <= min(hi, limit); d++ {
				res += dfs(i+1, limitLow && d == lo, limitHigh && d == hi)
			}
		} else { // This digit must be s[i-diff]
			x := int(s[i-diff] - '0')
			if lo <= x && x <= hi { // The problem guarantees x <= limit, so no check is needed
				res += dfs(i+1, limitLow && x == lo, limitHigh && x == hi)
			}
		}
		return
	}
	return dfs(0, true, true)
}
```

## Template 2.1

```python3
# Example: count numbers in [low, high] that contain exactly target zeros
# For example, digitDP(0, 10, 1) == 2
# When counting zeros, distinguish leading zeros from zeros within the number; exclude the former and count the latter
def digitDP(low: int, high: int, target: int) -> int:
    low_s = list(map(int, str(low)))  # Avoid repeated int() calls in dfs
    high_s = list(map(int, str(high)))
    n = len(high_s)
    diff_lh = n - len(low_s)

    @cache
    def dfs(i: int, cnt0: int, limit_low: bool, limit_high: bool) -> int:
        if cnt0 > target:
            return 0  # Invalid
        if i == n:
            return 1 if cnt0 == target else 0

        lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
        hi = high_s[i] if limit_high else 9

        res = 0
        start = lo

        # limit_low and i determine whether a digit can be skipped, so no is_num parameter is needed
        # Remove this if block if leading zeros do not affect the answer
        if limit_low and i < diff_lh:
            # Skip this digit; the upper bound no longer applies
            res = dfs(i + 1, 0, True, False)
            start = 1

        for d in range(start, hi + 1):
            res += dfs(i + 1,
                       cnt0 + (1 if d == 0 else 0),  # Count zeros
                       limit_low and d == lo,
                       limit_high and d == hi)

        # res %= MOD
        return res

    return dfs(0, 0, True, True)
```
```c++
// Example: count numbers in [low, high] that contain exactly target zeros
// For example, digitDP(0, 10, 1) == 2
// When counting zeros, distinguish leading zeros from zeros within the number; exclude the former and count the latter
long long digitDP(long long low, long long high, int target) {
    string low_s = to_string(low);
    string high_s = to_string(high);
    int n = high_s.size();
    int diff_lh = n - low_s.size();
    vector memo(n, vector<long long>(target + 1, -1));

    auto dfs = [&](this auto&& dfs, int i, int cnt0, bool limit_low, bool limit_high) -> long long {
        if (cnt0 > target) {
            return 0; // Invalid
        }
        if (i == n) {
            return cnt0 == target;
        }

        if (!limit_low && !limit_high && memo[i][cnt0] >= 0) {
            return memo[i][cnt0];
        }

        int lo = limit_low && i >= diff_lh ? low_s[i - diff_lh] - '0' : 0;
        int hi = limit_high ? high_s[i] - '0' : 9;

        long long res = 0;
        int d = lo;

        // limit_low and i determine whether a digit can be skipped, so no is_num parameter is needed
        // Remove this if block if leading zeros do not affect the answer
        if (limit_low && i < diff_lh) {
            // Skip this digit; the upper bound no longer applies
            res = dfs(i + 1, 0, true, false);
            d = 1;
        }

        for (; d <= hi; d++) {
            // Count zeros
            res += dfs(i + 1, cnt0 + (d == 0), limit_low && d == lo, limit_high && d == hi);
            // res %= MOD;
        }

        if (!limit_low && !limit_high) {
            memo[i][cnt0] = res;
        }
        return res;
    };

    return dfs(0, 0, true, true);
}
```
