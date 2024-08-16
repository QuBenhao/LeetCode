package problemLCR_014

import (
	"encoding/json"
	"log"
	"strings"
)

func checkInclusion(s1 string, s2 string) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s1 string
	var s2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &s1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s2); err != nil {
		log.Fatal(err)
	}

	return checkInclusion(s1, s2)
}
