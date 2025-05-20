package problem3536

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProduct(n int) int {
	mx, subMax := 0, 0
	for ; n > 0; n /= 10 {
		cur := n % 10
		if cur > mx {
			subMax = mx
			mx = cur
		} else if cur > subMax {
			subMax = cur
		}
	}
	return mx * subMax
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return maxProduct(n)
}
