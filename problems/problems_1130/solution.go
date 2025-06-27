package problem1130

import (
	"encoding/json"
	"log"
	"strings"
)

func mctFromLeafValues(arr []int) (ans int) {
	var stack []int
	for _, v := range arr {
		for len(stack) > 0 && stack[len(stack)-1] <= v {
			mid := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if len(stack) == 0 || stack[len(stack)-1] > v {
				ans += mid * v
			} else {
				ans += mid * stack[len(stack)-1]
			}
		}
		stack = append(stack, v)
	}
	for len(stack) > 1 {
		mid := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ans += mid * stack[len(stack)-1]
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return mctFromLeafValues(arr)
}
