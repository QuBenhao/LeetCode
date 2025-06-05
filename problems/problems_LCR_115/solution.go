package problemLCR_115

import (
	"encoding/json"
	"log"
	"strings"
)

func sequenceReconstruction(nums []int, sequences [][]int) bool {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var sequences [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &sequences); err != nil {
		log.Fatal(err)
	}

	return sequenceReconstruction(nums, sequences)
}
