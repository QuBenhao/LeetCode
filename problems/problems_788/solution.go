package problem788

import (
	"encoding/json"
	"log"
	"strings"
)

var ans = make([]int, 10001)

func init() {
	for i := 1; i <= 10000; i++ {
		notRotatable := false
		diffRotatable := false
		for j := i; j > 0; j /= 10 {
			c := j % 10
			if c == 3 || c == 4 || c == 7 {
				notRotatable = true
				break
			}
			if c == 2 || c == 5 || c == 6 || c == 9 {
				diffRotatable = true
			}
		}
		ans[i] = ans[i-1]
		if !notRotatable && diffRotatable {
			ans[i]++
		}
	}
}

func rotatedDigits(n int) int {
	return ans[n]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return rotatedDigits(n)
}
