package problem2200

import (
	"encoding/json"
	"log"
	"strings"
)

func findKDistantIndices(nums []int, key int, k int) (ans []int) {
	last := -1
	n := len(nums)
	for i, num := range nums {
		if num != key {
			continue
		}
		last = max(last+1, i-k)
		end := min(i+k, n-1)
		for j := last; j <= end; j++ {
			ans = append(ans, j)
		}
		last = end
		if last >= n-1 {
			break
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var key int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &key); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return findKDistantIndices(nums, key, k)
}
