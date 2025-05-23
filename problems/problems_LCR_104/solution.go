package problemLCR_104

import (
	"encoding/json"
	"log"
	"strings"
)

func combinationSum4(nums []int, target int) int {

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

	return combinationSum4(nums, target)
}
