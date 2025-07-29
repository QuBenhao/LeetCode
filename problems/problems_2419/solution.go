package problem2419

import (
	"encoding/json"
	"log"
	"strings"
)

func longestSubarray(nums []int) (ans int) {
	cur, mx := 0, 0
	for _, num := range nums {
		if num > mx {
			cur = 1
			ans = 1
			mx = num
		} else if num == mx {
			cur++
			if cur > ans {
				ans = cur
			}
		} else {
			cur = 0
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return longestSubarray(nums)
}
