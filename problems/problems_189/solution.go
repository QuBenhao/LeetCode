package problem189

import (
	"encoding/json"
	"log"
	"strings"
)

func rotate(nums []int, k int) {
	reverse := func(i int, j int) {
		for i < j {
			nums[i], nums[j] = nums[j], nums[i]
			i++
			j--
		}
	}
	n := len(nums)
	reverse(0, n-1)
	reverse(0, k%n-1)
	reverse(k%n, n-1)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	rotate(nums, k)
	return nums
}
