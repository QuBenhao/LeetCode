package problem2012

import (
	"encoding/json"
	"log"
	"strings"
)

func sumOfBeauties(nums []int) (ans int) {
	n := len(nums)
	sufMin := make([]int, n)
	sufMin[n-1] = nums[n-1]
	for i := n - 2; i >= 0; i-- {
		sufMin[i] = min(sufMin[i+1], nums[i])
	}
	preMax := nums[0]
	for i := 1; i < n-1; i++ {
		if preMax < nums[i] && nums[i] < sufMin[i+1] {
			ans += 2
		} else if nums[i-1] < nums[i] && nums[i] < nums[i+1] {
			ans++
		}
		preMax = max(preMax, nums[i])
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return sumOfBeauties(nums)
}
