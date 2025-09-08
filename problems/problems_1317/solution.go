package problem1317

import (
	"encoding/json"
	"log"
	"strings"
)

func getNoZeroIntegers(n int) []int {
	a := 0
	base := 1
	x := n
	for x > 1 {
		d := x % 10
		x /= 10
		if d <= 1 {
			d += 10
			x -= 1
		}
		a += (d / 2) * base
		base *= 10
	}
	return []int{a, n - a}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return getNoZeroIntegers(n)
}
