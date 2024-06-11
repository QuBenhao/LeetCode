package problem54

import (
	"encoding/json"
	"log"
	"strings"
)

func spiralOrder(matrix [][]int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(values[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return spiralOrder(matrix)
}
