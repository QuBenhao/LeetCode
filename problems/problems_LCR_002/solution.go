package problemLCR_002

import (
	"encoding/json"
	"log"
	"strings"
)

func addBinary(a string, b string) string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var a string
	var b string

	if err := json.Unmarshal([]byte(inputValues[0]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &b); err != nil {
		log.Fatal(err)
	}

	return addBinary(a, b)
}
