package problem1695

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumUniqueSubarray(nums []int) (ans int) {
	left, cur := 0, 0
	seen := make(map[int]bool)
	for _, num := range nums {
		for seen[num] {
			seen[nums[left]] = false
			cur -= nums[left]
			left++
		}
		seen[num] = true
		cur += num
		if cur > ans {
			ans = cur
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maximumUniqueSubarray(nums)
}
