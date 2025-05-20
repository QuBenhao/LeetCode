package problem2274

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxConsecutive(bottom int, top int, special []int) (ans int) {
	nums := make([]int, len(special)+2)
	copy(nums, special)
	nums[len(nums)-2] = bottom - 1
	nums[len(nums)-1] = top + 1
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		ans = max(ans, nums[i]-nums[i-1]-1)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bottom int
	var top int
	var special []int

	if err := json.Unmarshal([]byte(inputValues[0]), &bottom); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &top); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &special); err != nil {
		log.Fatal(err)
	}

	return maxConsecutive(bottom, top, special)
}
