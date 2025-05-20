package problem219

import (
	"encoding/json"
	"log"
	"strings"
)

func containsNearbyDuplicate(nums []int, k int) bool {
	idxMap := map[int]any{}
	for i, num := range nums {
		if _, ok := idxMap[num]; ok {
			return true
		}
		if i >= k {
			delete(idxMap, nums[i-k])
		}
		idxMap[num] = nil
	}
	return false
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

	return containsNearbyDuplicate(nums, k)
}
