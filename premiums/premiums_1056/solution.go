package problem1056

import (
	"encoding/json"
	"log"
	"strings"
)

func confusingNumber(n int) bool {
	trans := map[int]int{0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
	revert := 0
	for num := n; num > 0; num /= 10 {
		cur := num % 10
		if v, ok := trans[cur]; !ok {
			return false
		} else {
			revert = 10*revert + v
		}
	}
	return revert != n
}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var n int

	if err := json.Unmarshal([]byte(values[0]), &n); err != nil {
		log.Fatal(err)
	}

	return confusingNumber(n)
}
