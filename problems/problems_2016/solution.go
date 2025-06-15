package problem2016

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumDifference(nums []int) int {
    ans := -1
    mn := nums[0]
    for _, num := range nums {
        if num > mn {
            ans = max(ans, num-mn)
        }
        mn = min(mn, num)
    }
    return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maximumDifference(nums)
}
