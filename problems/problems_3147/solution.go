package problem3147

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maximumEnergy(energy []int, k int) int {
	n := len(energy)
	for i := n - k - 1; i >= 0; i-- {
		energy[i] += energy[i+k]
	}
	return slices.Max(energy)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var energy []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &energy); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximumEnergy(energy, k)
}
