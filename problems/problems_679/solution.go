package problem679

import (
	"encoding/json"
	"log"
	"strings"
)

func judgePoint24(cards []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cards []int

	if err := json.Unmarshal([]byte(inputValues[0]), &cards); err != nil {
		log.Fatal(err)
	}

	return judgePoint24(cards)
}
