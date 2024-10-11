package problemLCR_065

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumLengthEncoding(words []string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return minimumLengthEncoding(words)
}
