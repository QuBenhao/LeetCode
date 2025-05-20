package problemLCR_084

import (
	"encoding/json"
	"log"
	"strings"
)

func permuteUnique(nums []int) (ans [][]int) {
	var dfs func(int)
	dfs = func(u int) {
		if u == len(nums)-1 {
			ans = append(ans, append([]int(nil), nums...))
			return
		}
		vis := map[int]bool{}
		for i := u; i < len(nums); i++ {
			if vis[nums[i]] {
				continue
			}
			vis[nums[i]] = true
			nums[u], nums[i] = nums[i], nums[u]
			dfs(u + 1)
			nums[u], nums[i] = nums[i], nums[u]
		}
	}
	dfs(0)
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return permuteUnique(nums)
}
