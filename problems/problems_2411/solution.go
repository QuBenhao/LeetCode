package problem2411

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestSubarrays(nums []int) []int {
	ans := make([]int, len(nums))
	for i, x := range nums {
		ans[i] = 1
		for j := i - 1; j >= 0; j-- {
			if (nums[j] | x) == nums[j] {
				break
			}
			nums[j] |= x
			ans[j] = i - j + 1
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return smallestSubarrays(nums)
}
