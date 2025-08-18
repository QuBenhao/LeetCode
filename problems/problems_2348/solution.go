package problem2348

import (
	"encoding/json"
	"log"
	"strings"
)

func zeroFilledSubarray(nums []int) (ans int64) {
	n := len(nums)
	left := 0
	for right := 0; right < n; right++ {
		for left < n && nums[left] != 0 {
			left++
		}
		right = left
		for right < n && nums[right] == 0 {
			right++
		}
		ans += int64(right-left) * int64(right-left+1) / 2
		left = right
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return zeroFilledSubarray(nums)
}
