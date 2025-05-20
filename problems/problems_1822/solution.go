package problem1822

import (
	"encoding/json"
	"log"
	"strings"
)

func arraySign(nums []int) int {
	cnt := 0
	for _, num := range nums {
		if num == 0 {
			return 0
		} else if num < 0 {
			cnt++
		}
	}
	if cnt%2 != 0 {
		return -1
	}
	return 1
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return arraySign(nums)
}
