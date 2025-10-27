package problem3354

import (
	"encoding/json"
	"log"
	"strings"
)

func countValidSelections(nums []int) (ans int) {
	total := 0
	for _, x := range nums {
		total += x
	}

	pre := 0
	for _, x := range nums {
		if x > 0 {
			pre += x
		} else if pre*2 == total {
			ans += 2
		} else if abs(pre*2-total) == 1 {
			ans++
		}
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countValidSelections(nums)
}
