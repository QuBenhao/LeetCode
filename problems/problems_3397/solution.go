package problem3397

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxDistinctElements(nums []int, k int) (ans int) {
	sort.Ints(nums)
	cur := nums[0] - k - 1
	for _, num := range nums {
		if num+k == cur {
			continue
		}
		ans++
		if d := num - k; d > cur {
			cur = d
		} else {
			cur++
		}
	}
	return
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

	return maxDistinctElements(nums, k)
}
