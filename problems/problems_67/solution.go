package problem67

import (
	"encoding/json"
	"log"
	"strings"
)

func addBinary(a string, b string) string {
	if len(b) > len(a) {
		a, b = b, a
	}
	ans := make([]byte, len(a)+1)
	idx, cur := len(a), 0
	for i := len(b) - 1; i >= 0; i-- {
		if a[i+len(a)-len(b)] == '1' {
			cur++
		}
		if b[i] == '1' {
			cur++
		}
		if cur%2 == 0 {
			ans[idx] = '0'
		} else {
			ans[idx] = '1'
		}
		cur /= 2
		idx--
	}
	for i := len(a) - len(b) - 1; i >= 0; i-- {
		if a[i] == '1' {
			cur++
		}
		if cur%2 == 0 {
			ans[idx] = '0'
		} else {
			ans[idx] = '1'
		}
		cur /= 2
		idx--
	}
	if cur > 0 {
		ans[idx] = '1'
	} else {
		idx++
	}
	return string(ans[idx:])
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var a string
	var b string

	if err := json.Unmarshal([]byte(values[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &b); err != nil {
		log.Fatal(err)
	}

	return addBinary(a, b)
}
