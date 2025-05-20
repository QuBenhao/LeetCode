package problem1742

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func countBalls(lowLimit int, highLimit int) (ans int) {
	low := strconv.FormatInt(int64(lowLimit), 10)
	high := strconv.FormatInt(int64(highLimit), 10)
	n := len(high)
	low = strings.Repeat("0", n-len(low)) + low // 补前导零，和 high 对齐

	m := int(high[0]-'0') + (n-1)*9
	memo := make([][]int64, n)
	for i := range memo {
		memo[i] = make([]int64, m+1)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dfs func(int, int, bool, bool) int64
	dfs = func(i, j int, limitLow, limitHigh bool) (res int64) {
		if i == n {
			if j == 0 {
				return 1
			}
			return
		}

		if !limitLow && !limitHigh {
			p := &memo[i][j]
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

		for d := lo; d <= min(hi, j); d++ {
			res += dfs(i+1, j-d, limitLow && d == lo, limitHigh && d == hi)
		}
		return
	}
	for j := 1; j <= m; j++ {
		ans = max(ans, int(dfs(0, j, true, true)))
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lowLimit int
	var highLimit int

	if err := json.Unmarshal([]byte(inputValues[0]), &lowLimit); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &highLimit); err != nil {
		log.Fatal(err)
	}

	return countBalls(lowLimit, highLimit)
}
