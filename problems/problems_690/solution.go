package problem690

import (
	"encoding/json"
	"log"
	"strings"
)

/**
 * Definition for Employee.
 * type Employee struct {
 *     Id int
 *     Importance int
 *     Subordinates []int
 * }
 */

func getImportance(employees []*Employee, id int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var employees []*Employee
	var id int

	if err := json.Unmarshal([]byte(inputValues[0]), &employees); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &id); err != nil {
		log.Fatal(err)
	}

	return getImportance(employees, id)
}
