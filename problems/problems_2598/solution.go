package problem2598

import (
	"encoding/json"
	"log"
	"strings"
)

func findSmallestInteger(nums []int, value int) int {
	counts := make([]int, value)
	for _, num := range nums {
		counts[(num%value+value)%value]++
	}
	ansM, ans := counts[0], 0
	for i, v := range counts {
		if v < ansM {
			ansM, ans = v, i
		}
	}
	return value*ansM + ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var value int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &value); err != nil {
		log.Fatal(err)
	}

	return findSmallestInteger(nums, value)
}
