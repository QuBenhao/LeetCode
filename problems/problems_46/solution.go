package problem46

import (
	"encoding/json"
	"log"
	"strings"
)

func permute(nums []int) (ans [][]int) {
	var backtrack func(int)
	backtrack = func(idx int) {
		if idx == len(nums) {
			tmp := make([]int, len(nums))
			copy(tmp, nums)
			ans = append(ans, tmp)
			return
		}
		for i := idx; i < len(nums); i++ {
			nums[i], nums[idx] = nums[idx], nums[i]
			backtrack(idx + 1)
			nums[i], nums[idx] = nums[idx], nums[i]
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
