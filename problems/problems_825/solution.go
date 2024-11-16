package problem825

import (
	"encoding/json"
	"log"
	"strings"
)

func numFriendRequests(ages []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var ages []int

	if err := json.Unmarshal([]byte(inputValues[0]), &ages); err != nil {
		log.Fatal(err)
	}

	return numFriendRequests(ages)
}
