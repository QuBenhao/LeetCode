package problem2024

import (
	"encoding/json"
	"log"
	"strings"
)

func maxConsecutiveAnswers(answerKey string, k int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var answerKey string
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &answerKey); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maxConsecutiveAnswers(answerKey, k)
}
