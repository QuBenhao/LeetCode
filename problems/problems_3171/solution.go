package problem3171

import (
	"encoding/json"
	"log"
	"strings"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func minimumDifference(nums []int, k int) int {
	ans := abs(nums[0] - k)
	for i := 1; i < len(nums); i++ {
		ans = min(ans, abs(nums[i]-k))
		for j := i - 1; j >= 0 && nums[j]|nums[i] != nums[j]; j-- {
			nums[j] |= nums[i]
			ans = min(ans, abs(nums[j]-k))
		}
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return minimumDifference(nums, k)
}
