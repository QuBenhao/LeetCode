package problem66

import (
	"encoding/json"
	"log"
	"strings"
)

func plusOne(digits []int) []int {
	cur := 1
	for i := len(digits) - 1; i >= 0 && cur > 0; i-- {
		cur += digits[i]
		digits[i] = cur % 10
		cur /= 10
	}
	if cur > 0 {
		arr := make([]int, len(digits)+1)
		arr[0] = cur
		return arr
	}
	return digits
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var digits []int

	if err := json.Unmarshal([]byte(values[0]), &digits); err != nil {
		log.Fatal(err)
	}

	return plusOne(digits)
}
