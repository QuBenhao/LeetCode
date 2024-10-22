package problem3184

import (
	"encoding/json"
	"log"
	"strings"
)

func countCompleteDayPairs(hours []int) (ans int) {
	hs := make([]int, 24)
	for _, h := range hours {
		hs[h%24]++
	}
	for i := 1; i < 12; i++ {
		ans += hs[i] * hs[24-i]
	}
	ans += hs[0] * (hs[0] - 1) / 2
	ans += hs[12] * (hs[12] - 1) / 2
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var hours []int

	if err := json.Unmarshal([]byte(inputValues[0]), &hours); err != nil {
		log.Fatal(err)
	}

	return countCompleteDayPairs(hours)
}
