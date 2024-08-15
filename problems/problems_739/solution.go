package problem739

import (
	"encoding/json"
	"log"
	"strings"
)

func dailyTemperatures(temperatures []int) []int {
	ans := make([]int, len(temperatures))
	var stack []int
	for i, t := range temperatures {
		for len(stack) > 0 && t > temperatures[stack[len(stack)-1]] {
			prev := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[prev] = i - prev
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
