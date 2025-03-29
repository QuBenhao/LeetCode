package problem2109

import (
	"encoding/json"
	"log"
	"strings"
)

func addSpaces(s string, spaces []int) string {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var spaces []int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &spaces); err != nil {
		log.Fatal(err)
	}

	return addSpaces(s, spaces)
}
