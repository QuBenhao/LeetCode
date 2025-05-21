package problemLCR_087

import (
	"encoding/json"
	"log"
	"strings"
)

func restoreIpAddresses(s string) (ans []string) {
	isValid := func(seg string) bool {
		if seg[0] == '0' && len(seg) > 1 {
			return false
		}
		num := 0
		for i := 0; i < len(seg); i++ {
			num = num*10 + int(seg[i]-'0')
		}
		return num <= 255
	}

	if len(s) < 4 || len(s) > 12 {
		return
	}
	var cur []string
	n := len(s)

	var backtrack func(int)
	backtrack = func(start int) {
		if start == n {
			return
		}
		if len(cur) == 3 {
			if n-start > 3 || (s[start] == '0' && start < n-1) {
				return
			}
			if isValid(s[start:]) {
				cur = append(cur, s[start:])
				ans = append(ans, strings.Join(cur, "."))
				cur = cur[:len(cur)-1]
			}
			return
		}
		if s[start] == '0' {
			cur = append(cur, "0")
			backtrack(start + 1)
			cur = cur[:len(cur)-1]
			return
		}
		for i := 1; i <= min(n-start, 3); i++ {
			seg := s[start : start+i]
			if isValid(seg) {
				cur = append(cur, seg)
				backtrack(start + i)
				cur = cur[:len(cur)-1]
			}
		}
	}
	backtrack(0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return restoreIpAddresses(s)
}
