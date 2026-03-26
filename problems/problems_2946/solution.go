package problem2946

import (
	"encoding/json"
	"log"
	"strings"
)

func areSimilar(mat [][]int, k int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return areSimilar(mat, k)
}
