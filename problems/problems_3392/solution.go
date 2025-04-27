package problem3392

import (
	"encoding/json"
	"log"
	"strings"
)

func countSubarrays(nums []int) (ans int) {
	for i, n := 0, len(nums)-2; i < n; i++ {
		if nums[i+1]%2 == 0 && nums[i+1]/2 == nums[i]+nums[i+2] {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countSubarrays(nums)
}
