package problem422

import (
	"encoding/json"
	"log"
	"strings"
)

func validWordSquare(words []string) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var words []string

	if err := json.Unmarshal([]byte(values[0]), &words); err != nil {
		log.Fatal(err)
	}

	return validWordSquare(words)
}
