package problemLCR_038

import (
	"encoding/json"
	"log"
	"strings"
)

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	ans := make([]int, n)
	var stack []int
	for i := 0; i < n; i++ {
		for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]] {
			prevIndex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[prevIndex] = i - prevIndex
		}
		stack = append(stack, i)
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var temperatures []int

	if err := json.Unmarshal([]byte(inputValues[0]), &temperatures); err != nil {
		log.Fatal(err)
	}

	return dailyTemperatures(temperatures)
}
