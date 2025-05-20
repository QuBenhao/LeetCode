package problem2272

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func largestVariance(s string) (ans int) {
	var f0, f1 [26][26]int
	for i := range f1 {
		for j := range f1[i] {
			f1[i][j] = math.MinInt
		}
	}

	for _, ch := range s {
		ch -= 'a'
		// 遍历到 ch 时，只需计算 a=ch 或者 b=ch 的状态，其他状态和 ch 无关，f 值不变
		for i := range 26 {
			if i == int(ch) {
				continue
			}
			// 假设出现次数最多的字母 a=ch，更新所有 b=i 的状态
			f0[ch][i] = max(f0[ch][i], 0) + 1
			f1[ch][i]++
			// 假设出现次数最少的字母 b=ch，更新所有 a=i 的状态
			f0[i][ch] = max(f0[i][ch], 0) - 1
			f1[i][ch] = f0[i][ch]
			ans = max(ans, f1[ch][i], f1[i][ch])
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return largestVariance(s)
}
