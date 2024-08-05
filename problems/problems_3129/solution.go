package problem3129

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfStableArrays(zero int, one int, limit int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var zero int
	var one int
	var limit int

	if err := json.Unmarshal([]byte(inputValues[0]), &zero); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &one); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &limit); err != nil {
		log.Fatal(err)
	}

	return numberOfStableArrays(zero, one, limit)
}
