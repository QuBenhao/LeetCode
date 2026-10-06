package problem2376

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
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
				return 1 // A valid number has been formed
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
		if !isNum { // The current digit can be skipped
			res += dfs(i+1, mask, false, false)
		}
		d := 0
		if !isNum {
			d = 1 // If no digit has been placed, start at 1 to avoid leading zeros
		}
		up := 9
		if isLimit {
			up = int(s[i] - '0') // If all previous digits match n, this digit can be at most s[i] (otherwise the number would exceed n)
		}
		for ; d <= up; d++ { // Enumerate the digit d to place
			if mask>>d&1 == 0 { // If d is absent from mask, it has not been used before
				res += dfs(i+1, mask|1<<d, isLimit && d == up, true)
			}
		}
		return
	}
	return dfs(0, 0, true, false)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countSpecialNumbers(n)
}
