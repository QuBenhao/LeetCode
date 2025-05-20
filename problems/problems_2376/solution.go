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

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countSpecialNumbers(n)
}
