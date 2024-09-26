package problem2535

import (
	"encoding/json"
	"log"
	"strings"
)

func differenceOfSum(nums []int) (ans int) {
	for _, num := range nums {
		ans += num
		for num > 0 {
			ans -= num % 10
			num /= 10
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

	return differenceOfSum(nums)
}
