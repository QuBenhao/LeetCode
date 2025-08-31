package problem3668

import (
	"encoding/json"
	"log"
	"strings"
)

func recoverOrder(order []int, friends []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var order []int
	var friends []int

	if err := json.Unmarshal([]byte(inputValues[0]), &order); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &friends); err != nil {
		log.Fatal(err)
	}

	return recoverOrder(order, friends)
}
