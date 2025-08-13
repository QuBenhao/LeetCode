package problem1780

import (
	"encoding/json"
	"log"
	"strings"
)

func checkPowersOfThree(n int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return checkPowersOfThree(n)
}
