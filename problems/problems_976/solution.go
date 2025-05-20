package problem976

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func largestPerimeter(nums []int) int {
	slices.Sort(nums)
	for i := len(nums) - 1; i > 1; i-- {
		if nums[i] < nums[i-1]+nums[i-2] {
			return nums[i] + nums[i-1] + nums[i-2]
		}
	}
	return 0
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return largestPerimeter(nums)
}
