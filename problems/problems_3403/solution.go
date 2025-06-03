package problem3403

import (
	"encoding/json"
	"log"
	"strings"
)

func answerString(word string, numFriends int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word string
	var numFriends int

	if err := json.Unmarshal([]byte(inputValues[0]), &word); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &numFriends); err != nil {
		log.Fatal(err)
	}

	return answerString(word, numFriends)
}
