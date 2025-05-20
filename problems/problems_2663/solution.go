package problem2663

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestBeautifulString(S string, k int) string {
	limit := 'a' + byte(k)
	s := []byte(S)
	n := len(s)
	i := n - 1 // 从最后一个字母开始
	s[i]++     // 先加一
	for i < n {
		if s[i] == limit { // 需要进位
			if i == 0 { // 无法进位
				return ""
			}
			// 进位
			s[i] = 'a'
			i--
			s[i]++
		} else if i > 0 && s[i] == s[i-1] || i > 1 && s[i] == s[i-2] {
			s[i]++ // 如果 s[i] 和左侧的字符形成回文串，就继续增加 s[i]
		} else {
			i++ // 反过来检查后面是否有回文串
		}
	}
	return string(s)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string
	var k int

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return smallestBeautifulString(s, k)
}
