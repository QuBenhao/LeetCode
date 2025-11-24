package problem1015

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestRepunitDivByK(k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}

	return smallestRepunitDivByK(k)
}
