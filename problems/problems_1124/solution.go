package problem1124

import (
	"encoding/json"
	"log"
	"strings"
)

func longestWPI(hours []int) (ans int) {
	prefixSum := 0
	prefixMap := map[int]int{0: -1}
	for i, hour := range hours {
		if hour > 8 {
			prefixSum++
		} else {
			prefixSum--
		}
		if _, exists := prefixMap[prefixSum]; !exists {
			prefixMap[prefixSum] = i
		}
		if prefixSum > 0 {
			ans = i + 1
		} else if startIndex, exists := prefixMap[prefixSum-1]; exists {
			ans = max(ans, i-startIndex)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var hours []int

	if err := json.Unmarshal([]byte(inputValues[0]), &hours); err != nil {
		log.Fatal(err)
	}

	return longestWPI(hours)
}
