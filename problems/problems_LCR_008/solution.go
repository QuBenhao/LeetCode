package problemLCR_008

import (
	"encoding/json"
	"log"
	"strings"
)

func minSubArrayLen(target int, nums []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target int
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums); err != nil {
		log.Fatal(err)
	}

	return minSubArrayLen(target, nums)
}
