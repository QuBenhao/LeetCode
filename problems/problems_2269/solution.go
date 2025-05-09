package problem2269

import (
	"encoding/json"
	"log"
	"math"
	"slices"
	"strings"
)

func divisorSubstrings(num int, k int) (ans int) {
	power := int(math.Pow(10, float64(k-1)))
	var nums []int
	for val := num; val > 0; val /= 10 {
		nums = append(nums, val%10)
	}
	slices.Reverse(nums)
	cur := 0
	for i, v := range nums {
		cur = cur*10 + v
		if i >= k-1 {
			if cur != 0 && num%cur == 0 {
				ans++
			}
			cur -= nums[i+1-k] * power
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return divisorSubstrings(num, k)
}
