package problem1304

import (
	"encoding/json"
	"log"
	"strings"
)

func sumZero(n int) []int {
	ans := make([]int, n)
	for i := range n / 2 {
		ans[i*2] = -i - 1
		ans[i*2+1] = i + 1
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return sumZero(n)
}
