package problem215

import (
	"encoding/json"
	"log"
	"math/rand"
	"strings"
)

func findKthLargest(nums []int, k int) int {
	pivot := nums[rand.Intn(len(nums))]
	lefts := make([]int, 0)
	rights := make([]int, 0)
	equals := make([]int, 0)
	for _, num := range nums {
		if num < pivot {
			lefts = append(lefts, num)
		} else if num > pivot {
			rights = append(rights, num)
		} else {
			equals = append(equals, num)
		}
	}
	if d := k - len(rights); d <= 0 {
		return findKthLargest(rights, k)
	} else if d1 := d - len(equals); d1 <= 0 {
		return pivot
	} else {
		return findKthLargest(lefts, d1)
	}
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

	return findKthLargest(nums, k)
}
