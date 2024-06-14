package problem73

import (
	"encoding/json"
	"log"
	"strings"
)

func setZeroes(matrix [][]int)  {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(values[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	setZeroes(matrix)
	return matrix
}
