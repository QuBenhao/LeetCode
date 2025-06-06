package problemLCR_115

import (
	"encoding/json"
	"log"
	"strings"
)

func sequenceReconstruction(nums []int, sequences [][]int) bool {
	hash := func(prev, next int) int {
		return prev<<14 | next
	}
	set, length := map[int]bool{}, 0
	for _, seq := range sequences {
		for i := 0; i < len(seq)-1; i++ {
			set[hash(seq[i], seq[i+1])] = true
		}
		length += len(seq)
	}
	for i := 0; i < len(nums)-1; i++ {
		if !set[hash(nums[i], nums[i+1])] {
			return false
		}
	}
	return len(set) > 0 || length == len(nums)
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
