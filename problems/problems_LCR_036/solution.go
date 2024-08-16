package problemLCR_036

import (
	"encoding/json"
	"log"
	"strings"
)

func evalRPN(tokens []string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tokens []string

	if err := json.Unmarshal([]byte(inputValues[0]), &tokens); err != nil {
		log.Fatal(err)
	}

	return evalRPN(tokens)
}
