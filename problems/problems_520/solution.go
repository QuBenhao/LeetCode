package problem520

import (
	"encoding/json"
	"log"
	"strings"
)

func detectCapitalUse(word string) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var word string

	if err := json.Unmarshal([]byte(values[0]), &word); err != nil {
		log.Fatal(err)
	}

	return detectCapitalUse(word)
}
