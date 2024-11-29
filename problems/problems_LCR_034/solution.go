package problemLCR_034

import (
	"encoding/json"
	"log"
	"strings"
)

func isAlienSorted(words []string, order string) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var order string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &order); err != nil {
		log.Fatal(err)
	}

	return isAlienSorted(words, order)
}
