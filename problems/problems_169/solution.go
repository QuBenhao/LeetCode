package problem169

import (
	"encoding/json"
	"log"
	"strings"
)

func majorityElement(nums []int) (ans int) {
	cnt := 0
	for _, num := range nums {
		if cnt != 0 && ans != num {
			cnt--
		} else {
			ans = num
			cnt++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return majorityElement(nums)
}
