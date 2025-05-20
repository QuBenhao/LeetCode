package problem2553

import (
	"encoding/json"
	"log"
	"strings"
)

func separateDigits(nums []int) (ans []int) {
	for _, num := range nums {
		var cur []int
		for num > 0 {
			cur = append(cur, num%10)
			num /= 10
		}
		for i := len(cur) - 1; i >= 0; i-- {
			ans = append(ans, cur[i])
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

	return separateDigits(nums)
}
