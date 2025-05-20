package problem31

import (
	"encoding/json"
	"log"
	"strings"
)

func nextPermutation(nums []int) {
	reverse := func(i int, j int) {
		for i < j {
			nums[i], nums[j] = nums[j], nums[i]
			i++
			j--
		}
	}
	n := len(nums)
	idx := n - 1
	for idx > 0 && nums[idx-1] >= nums[idx] {
		idx--
	}
	if idx == 0 {
		reverse(0, n-1)
		return
	}
	i := n - 1
	for i >= idx && nums[i] <= nums[idx-1] {
		i--
	}
	nums[i], nums[idx-1] = nums[idx-1], nums[i]
	reverse(idx, n-1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	nextPermutation(nums)
	return nums
}
