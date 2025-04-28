package problem2962

import (
	"encoding/json"
	"log"
	"strings"
)

func countSubarrays(nums []int, k int) (ans int64) {
	n, left, right, cur, mx := len(nums), 0, 0, 0, 0
	for _, num := range nums {
		mx = max(mx, num)
	}
	for right < n {
		if nums[right] == mx {
			cur++
		}
		for cur >= k {
			ans += int64(n - right)
			if nums[left] == mx {
				cur--
			}
			left++
		}
		right++
	}
	return
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

	return countSubarrays(nums, k)
}
