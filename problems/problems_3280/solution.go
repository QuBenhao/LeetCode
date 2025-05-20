package problem3280

import (
	"encoding/json"
	"log"
	"strings"
)

func convertDateToBinary(date string) string {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var date string

	if err := json.Unmarshal([]byte(inputValues[0]), &date); err != nil {
		log.Fatal(err)
	}

	return convertDateToBinary(date)
}
