package problem163

import (
	"encoding/json"
	"log"
	"strings"
)

func findMissingRanges(nums []int, lower int, upper int) (ans [][]int) {
	nums = append(nums, upper+1)
	last := lower - 1
	for _, num := range nums {
		if d := num - last; d > 1 {
			ans = append(ans, []int{last + 1, num - 1})
		}
		last = num
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var lower int
	var upper int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &lower); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &upper); err != nil {
		log.Fatal(err)
	}

	return findMissingRanges(nums, lower, upper)
}
