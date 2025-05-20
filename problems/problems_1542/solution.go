package problem1542

import (
	"encoding/json"
	"log"
	"strings"
)

func longestAwesome(s string) (ans int) {
	const D = 10 // s 中的字符种类数
	n := len(s)
	pos := [1 << D]int{}
	for i := range pos {
		pos[i] = n // n 表示没有找到异或前缀和
	}
	pos[0] = -1 // pre[-1] = 0
	pre := 0
	for i, c := range s {
		pre ^= 1 << (c - '0')
		for d := 0; d < D; d++ {
			ans = max(ans, i-pos[pre^(1<<d)]) // 奇数
		}
		ans = max(ans, i-pos[pre]) // 偶数
		if pos[pre] == n {         // 首次遇到值为 pre 的前缀异或和，记录其下标 i
			pos[pre] = i
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return longestAwesome(s)
}
