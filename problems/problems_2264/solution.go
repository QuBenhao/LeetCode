package problem2264

import (
	"encoding/json"
	"log"
	"strings"
)

func largestGoodInteger(num string) string {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return largestGoodInteger(num)
}
