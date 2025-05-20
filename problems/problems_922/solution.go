package problem922

import (
	"encoding/json"
	"log"
	"strings"
)

func sortArrayByParityII(nums []int) []int {
	n := len(nums)
	for i, j := 0, 1; i < n && j < n; {
		for ; i < n && nums[i]%2 == 0; i += 2 {
		}
		for ; j < n && nums[j]%2 == 1; j += 2 {
		}
		if i < n && j < n {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	return nums
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return sortArrayByParityII(nums)
}
