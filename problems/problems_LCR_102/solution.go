package problemLCR_102

import (
	"encoding/json"
	"log"
	"strings"
)

func findTargetSumWays(nums []int, target int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return findTargetSumWays(nums, target)
}
