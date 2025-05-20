package problem3270

import (
	"encoding/json"
	"log"
	"strings"
)

func generateKey(num1 int, num2 int, num3 int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num1 int
	var num2 int
	var num3 int

	if err := json.Unmarshal([]byte(inputValues[0]), &num1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &num2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &num3); err != nil {
		log.Fatal(err)
	}

	return generateKey(num1, num2, num3)
}
