package problem136

import (
	"encoding/json"
	"log"
	"strings"
)

func singleNumber(nums []int) (ans int) {
	for _, num := range nums {
		ans ^= num
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return singleNumber(nums)
}
