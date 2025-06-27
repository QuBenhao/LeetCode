package problem228

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func summaryRanges(nums []int) (ans []string) {
	n := len(nums)
	var left, right int
	for i := range n + 1 {
		if i == 0 || i == n || nums[i] != nums[i-1]+1 {
			if i != 0 {
				if left == right {
					ans = append(ans, strconv.Itoa(left))
				} else {
					ans = append(ans, strconv.Itoa(left)+"->"+strconv.Itoa(right))
				}
			}
			if i < n {
				left, right = nums[i], nums[i]
			}
		} else {
			right++
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

	return summaryRanges(nums)
}
