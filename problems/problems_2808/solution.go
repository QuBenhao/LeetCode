package problem2808

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumSeconds(nums []int) int {
	idxMap := map[int][]int{}
	for i, num := range nums {
		idxMap[num] = append(idxMap[num], i)
	}
	n := len(nums)
	ans := n
	for _, idxes := range idxMap {
		cur := idxes[0] + n - idxes[len(idxes)-1]
		for i := 1; i < len(idxes); i++ {
			cur = max(cur, idxes[i]-idxes[i-1])
		}
		ans = min(ans, cur)
	}
	return ans / 2
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minimumSeconds(nums)
}
