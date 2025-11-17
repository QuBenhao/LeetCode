package problem717

import (
	"encoding/json"
	"log"
	"strings"
)

func isOneBitCharacter(bits []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bits []int

	if err := json.Unmarshal([]byte(inputValues[0]), &bits); err != nil {
		log.Fatal(err)
	}

	return isOneBitCharacter(bits)
}
