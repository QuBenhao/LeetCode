package problem2848

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func numberOfPoints(nums [][]int) (ans int) {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i][0] < nums[j][0]
	})
	cur := nums[0][0] - 1
	for _, p := range nums {
		left, right := p[0], p[1]
		if left > cur {
			ans += right - left + 1
			cur = right
		} else if right > cur {
			ans += right - cur
			cur = right
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return numberOfPoints(nums)
}
