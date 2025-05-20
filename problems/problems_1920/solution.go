package problem1920

import (
	"encoding/json"
	"log"
	"strings"
)

func buildArray(nums []int) []int {
	for i, num := range nums {
		if num < 0 {
			continue
		}
		cur := i
		for nums[cur] != i {
			nxt := nums[cur]
			nums[cur] = ^nums[nxt]
			cur = nxt
		}
		nums[cur] = ^num
	}
	for i, num := range nums {
		nums[i] = ^num
	}
	return nums
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return buildArray(nums)
}
