package problem3423

import (
	"encoding/json"
	"log"
	"strings"
)

func maxAdjacentDistance(nums []int) int {
	absSub := func(a, b int) int {
		if a < b {
			return b - a
		}
		return a - b
	}
	ans := absSub(nums[0], nums[len(nums)-1])
	for i := range len(nums) - 1 {
		ans = max(ans, absSub(nums[i], nums[i+1]))
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxAdjacentDistance(nums)
}
