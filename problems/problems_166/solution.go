package problem166

import (
	"encoding/json"
	"log"
	"strings"
)

func fractionToDecimal(numerator int, denominator int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numerator int
	var denominator int

	if err := json.Unmarshal([]byte(inputValues[0]), &numerator); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &denominator); err != nil {
		log.Fatal(err)
	}

	return fractionToDecimal(numerator, denominator)
}
