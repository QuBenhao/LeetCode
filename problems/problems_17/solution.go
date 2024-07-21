package problem17

import (
	"encoding/json"
	"log"
	"strings"
)

func letterCombinations(digits string) []string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var digits string

	if err := json.Unmarshal([]byte(inputValues[0]), &digits); err != nil {
		log.Fatal(err)
	}

	return letterCombinations(digits)
}
