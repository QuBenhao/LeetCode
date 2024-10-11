package problem3158

import (
	"encoding/json"
	"log"
	"strings"
)

func duplicateNumbersXOR(nums []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return duplicateNumbersXOR(nums)
}
