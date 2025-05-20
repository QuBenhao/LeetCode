package problem2999

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfPowerfulInt(start int64, finish int64, limit int, s string) int64 {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var start int64
	var finish int64
	var limit int
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &start); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &finish); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &limit); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &s); err != nil {
		log.Fatal(err)
	}

	return numberOfPowerfulInt(start, finish, limit, s)
}
