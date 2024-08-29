package problem45

import (
	"encoding/json"
	"log"
	"strings"
)

func jump(nums []int) (ans int) {
	for cur, nxt, n := 0, 0, len(nums); nxt < n-1; ans++ {
		tmp := nxt
		for i := cur; i <= tmp; i++ {
			nxt = max(nxt, i+nums[i])
		}
		cur = tmp + 1
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return jump(nums)
}
