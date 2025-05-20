package problem3274

import (
	"encoding/json"
	"log"
	"strings"
)

func checkTwoChessboards(coordinate1 string, coordinate2 string) bool {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coordinate1 string
	var coordinate2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &coordinate1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &coordinate2); err != nil {
		log.Fatal(err)
	}

	return checkTwoChessboards(coordinate1, coordinate2)
}
