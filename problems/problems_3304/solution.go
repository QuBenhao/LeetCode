package problem3304

import (
	"encoding/json"
	"log"
	"strings"
)

func kthCharacter(k int) byte {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}

	return kthCharacter(k)
}
