package problemLCR_083

import (
	"encoding/json"
	"log"
	"strings"
)

func permute(nums []int) (ans [][]int) {
	var backtrack func(int)
	backtrack = func(first int) {
		if first == len(nums) {
			ans = append(ans, append([]int(nil), nums...))
			return
		}
		for i := first; i < len(nums); i++ {
			nums[first], nums[i] = nums[i], nums[first]
			backtrack(first + 1)
			nums[first], nums[i] = nums[i], nums[first]
		}
	}
	backtrack(0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return permute(nums)
}
