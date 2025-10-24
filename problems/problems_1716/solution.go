package problem1716

import (
	"encoding/json"
	"log"
	"strings"
)

func totalMoney(n int) int {
	d, r := n/7, n%7
	return 28*d + (d-1)*d*7/2 + r*(d+1+d+r)/2
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return totalMoney(n)
}
