package problem3186

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumTotalDamage(power []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var power []int

	if err := json.Unmarshal([]byte(inputValues[0]), &power); err != nil {
		log.Fatal(err)
	}

	return maximumTotalDamage(power)
}
