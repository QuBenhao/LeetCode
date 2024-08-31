package problemLCR_090

import (
	"encoding/json"
	"log"
	"strings"
)

func rob(nums []int) (ans int) {
	n := len(nums)
	dp_rob, dp_not_rob := nums[0], nums[0]
	for i := 2; i < n-1; i++ {
		dp_rob, dp_not_rob = dp_not_rob+nums[i], max(dp_rob, dp_not_rob)
	}
	ans = max(dp_rob, dp_not_rob)
	dp_rob, dp_not_rob = 0, 0
	for i := 1; i < n; i++ {
		dp_rob, dp_not_rob = dp_not_rob+nums[i], max(dp_rob, dp_not_rob)
	}
	ans = max(ans, max(dp_rob, dp_not_rob))
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return rob(nums)
}
