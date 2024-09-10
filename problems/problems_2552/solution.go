package problem2552

import (
	"encoding/json"
	"log"
	"strings"
)

func countQuadruplets(nums []int) (ans int64) {
	n := len(nums)
	cnt3 := make([]int64, n)
	for l := 2; l < n; l++ {
		var cnt2 int64
		for j := 0; j < l; j++ {
			if nums[j] < nums[l] {
				ans += cnt3[j]
				cnt2++
			} else {
				cnt3[j] += cnt2
			}
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countQuadruplets(nums)
}
