package problem3011

import (
	"encoding/json"
	"log"
	"strings"
)

func canSortArray(nums []int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return canSortArray(nums)
}
