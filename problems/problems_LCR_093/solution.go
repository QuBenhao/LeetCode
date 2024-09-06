package problemLCR_093

import (
	"encoding/json"
	"log"
	"strings"
)

func lenLongestFibSubseq(arr []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return lenLongestFibSubseq(arr)
}
