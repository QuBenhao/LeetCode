package problemInterview_05__02

import (
	"encoding/json"
	"log"
	"strings"
)

func printBin(num float64) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num float64

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return printBin(num)
}
