package problemLCR_096

import (
	"encoding/json"
	"log"
	"strings"
)

func isInterleave(s1 string, s2 string, s3 string) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s1 string
	var s2 string
	var s3 string

	if err := json.Unmarshal([]byte(inputValues[0]), &s1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &s3); err != nil {
		log.Fatal(err)
	}

	return isInterleave(s1, s2, s3)
}
