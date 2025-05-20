package problem2970

import (
	"encoding/json"
	"log"
	"strings"
)

func incremovableSubarrayCount(nums []int) int {
	n := len(nums)
	i := 0
	for i < n-1 && nums[i] < nums[i+1] {
		i++
	}
	if i == n-1 {
		return n * (n + 1) / 2
	}
	ans := i + 2
	j := n - 1
	for j == n-1 || nums[j] < nums[j+1] {
		for i >= 0 && nums[i] >= nums[j] {
			i--
		}
		ans += i + 2
		j--
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return incremovableSubarrayCount(nums)
}
