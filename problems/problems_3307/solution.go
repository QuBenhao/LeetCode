package problem3307

import (
	"encoding/json"
	"log"
	"strings"
)

func kthCharacter(k int64, operations []int) byte {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int64
	var operations []int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &operations); err != nil {
		log.Fatal(err)
	}

	return kthCharacter(k, operations)
}
