package problem1871

import (
	"encoding/json"
	"log"
	"strings"
)

func canReach(s string, minJump int, maxJump int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var minJump int
	var maxJump int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &minJump); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxJump); err != nil {
		log.Fatal(err)
	}

	return canReach(s, minJump, maxJump)
}
