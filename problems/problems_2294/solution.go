package problem2294

import (
	"encoding/json"
	"log"
	"math"
	"sort"
	"strings"
)

func partitionArray(nums []int, k int) (ans int) {
	sort.Ints(nums)
	cur := math.MinInt32
	for _, num := range nums {
		if num-cur > k {
			ans++
			cur = num
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

	return partitionArray(nums, k)
}
