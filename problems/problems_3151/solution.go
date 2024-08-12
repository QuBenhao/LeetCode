package problem3151

import (
	"encoding/json"
	"log"
	"strings"
)

func isArraySpecial(nums []int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return isArraySpecial(nums)
}
