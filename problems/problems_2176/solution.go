package problem2176

import (
	"encoding/json"
	"log"
	"strings"
)

func countPairs(nums []int, k int) (ans int) {
	n := len(nums)
	for i, num := range nums {
		for j := i + 1; j < n; j++ {
			if num == nums[j] && (i*j)%k == 0 {
				ans++
			}
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

	return countPairs(nums, k)
}
