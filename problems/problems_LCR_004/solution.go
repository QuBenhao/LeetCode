package problemLCR_004

import (
	"encoding/json"
	"log"
	"strings"
)

func singleNumber(nums []int) (one int) {
	two := 0
	for _, num := range nums {
		one = one ^ num & ^two
		two = two ^ num & ^one
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
