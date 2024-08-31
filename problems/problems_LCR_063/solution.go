package problemLCR_063

import (
	"encoding/json"
	"log"
	"strings"
)

func replaceWords(dictionary []string, sentence string) string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dictionary []string
	var sentence string

	if err := json.Unmarshal([]byte(inputValues[0]), &dictionary); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &sentence); err != nil {
		log.Fatal(err)
	}

	return replaceWords(dictionary, sentence)
}
