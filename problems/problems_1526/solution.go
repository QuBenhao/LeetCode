package problem1526

import (
	"encoding/json"
	"log"
	"strings"
)

func minNumberOperations(target []int) int {
    ans := target[0]
    for i := 1; i < len(target); i++ {
        ans += max(0, target[i] - target[i - 1])
    }
    return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target []int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}

	return minNumberOperations(target)
}
