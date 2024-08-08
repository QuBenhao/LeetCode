package problem22

import (
	"encoding/json"
	"log"
	"strings"
)

func generateParenthesis(n int) []string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return generateParenthesis(n)
}
