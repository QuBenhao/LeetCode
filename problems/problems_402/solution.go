package problem402

import (
	"encoding/json"
	"log"
	"strings"
)

func removeKdigits(num string, k int) string {
	var ans []rune
	for _, digit := range num {
		for k > 0 && len(ans) > 0 && ans[len(ans)-1] > rune(digit) {
			ans = ans[:len(ans)-1]
			k--
		}
		ans = append(ans, rune(digit))
	}
	ans = ans[:len(ans)-k] // Remove remaining k digits if any
	for len(ans) > 0 && ans[0] == '0' {
		ans = ans[1:] // Remove leading zeros
	}
	if len(ans) == 0 {
		return "0"
	}
	return string(ans)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return removeKdigits(num, k)
}
