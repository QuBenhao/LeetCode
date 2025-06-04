package problem1061

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s1 string
	var s2 string
	var baseStr string

	if err := json.Unmarshal([]byte(inputValues[0]), &s1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &baseStr); err != nil {
		log.Fatal(err)
	}

	return smallestEquivalentString(s1, s2, baseStr)
}
