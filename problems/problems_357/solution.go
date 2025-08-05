package problem357

import (
	"encoding/json"
	"log"
	"strings"
)

func countNumbersWithUniqueDigits(n int) int {
	if n == 0 {
		return 1
	}
	ans := 10
	last := 9
	for i := 2; i <= n; i++ {
		cur := last * (11 - i)
		ans += cur
		last = cur
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countNumbersWithUniqueDigits(n)
}
