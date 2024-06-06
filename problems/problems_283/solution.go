package problem283

import (
	"encoding/json"
	"log"
	"strings"
)

func moveZeroes(nums []int) {
	n, left := len(nums), 0
	for left = 0; left < n && nums[left] != 0; left++ {
	}
	for right := left + 1; right < n; right++ {
		for ; right < n && nums[right] == 0; right++ {
		}
		if right == n {
			break
		}
		nums[left], nums[right] = nums[right], nums[left]
		left++
	}
}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	moveZeroes(nums)
	return nums
}
