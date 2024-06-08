package problem43

import (
	"encoding/json"
	"log"
	"strings"
)

func multiply(num1 string, num2 string) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var num1 string
	var num2 string

	if err := json.Unmarshal([]byte(values[0]), &num1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &num2); err != nil {
		log.Fatal(err)
	}

	return multiply(num1, num2)
}
