package problem2099

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxSubsequence(nums []int, k int) []int {
	idxes := make([]int, len(nums))
	for i := range idxes {
		idxes[i] = i
	}
	sort.Slice(idxes, func(i, j int) bool {
		return nums[idxes[i]] > nums[idxes[j]]
	})
	idxes = idxes[:k]
	sort.Ints(idxes)
	for i, idx := range idxes {
		idxes[i] = nums[idx]
	}
	return idxes
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxSubsequence(nums, k)
}
