package problem3606

import (
	"encoding/json"
	"log"
	"strings"
)

func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var code []string
	var businessLine []string
	var isActive []bool

	if err := json.Unmarshal([]byte(inputValues[0]), &code); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &businessLine); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &isActive); err != nil {
		log.Fatal(err)
	}

	return validateCoupons(code, businessLine, isActive)
}
