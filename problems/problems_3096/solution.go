package problem3096

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumLevels(possible []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var possible []int

	if err := json.Unmarshal([]byte(inputValues[0]), &possible); err != nil {
		log.Fatal(err)
	}

	return minimumLevels(possible)
}
