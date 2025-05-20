package problem2974

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func numberGame(nums []int) (ans []int) {
	sort.Ints(nums)
	for i := 1; i < len(nums); i += 2 {
		ans = append(ans, nums[i])
		ans = append(ans, nums[i-1])
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return numberGame(nums)
}
