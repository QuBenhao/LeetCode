package problem2657

import (
	"encoding/json"
	"log"
	"strings"
)

func findThePrefixCommonArray(A []int, B []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var A []int
	var B []int

	if err := json.Unmarshal([]byte(inputValues[0]), &A); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &B); err != nil {
		log.Fatal(err)
	}

	return findThePrefixCommonArray(A, B)
}
