package problem2966

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func divideArray(nums []int, k int) (ans [][]int) {
	sort.Ints(nums)
	for i := 0; i < len(nums); i += 3 {
		if nums[i+2]-nums[i] > k {
			return [][]int{}
		}
		ans = append(ans, nums[i:i+3])
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

	return divideArray(nums, k)
}
