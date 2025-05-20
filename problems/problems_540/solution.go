package problem540

import (
	"encoding/json"
	"log"
	"strings"
)

func singleNonDuplicate(nums []int) (ans int) {
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

	return singleNonDuplicate(nums)
}
