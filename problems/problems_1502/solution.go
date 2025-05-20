package problem1502

import (
	"encoding/json"
	"log"
	"strings"
)

func canMakeArithmeticProgression(arr []int) bool {
	mn, mx := arr[0], arr[0]
	for _, num := range arr {
		mn, mx = min(mn, num), max(mx, num)
	}
	if (mx-mn)%(len(arr)-1) != 0 {
		return false
	}
	d := (mx - mn) / (len(arr) - 1)
	if d == 0 {
		return true
	}
	explored := make([]int, len(arr))
	for _, num := range arr {
		diff := num - mn
		if diff%d != 0 {
			return false
		}
		if explored[diff/d] != 0 {
			return false
		}
		explored[diff/d]++
	}
	return true
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(values[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return canMakeArithmeticProgression(arr)
}
