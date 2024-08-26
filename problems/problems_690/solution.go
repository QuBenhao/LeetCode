package problem690

import (
	"encoding/json"
	"log"
	"strings"
)

func getImportance(employees []*Employee, id int) int {
	employeeMap := make(map[int]*Employee)
	for _, employee := range employees {
		employeeMap[employee.Id] = employee
	}
	var dfs func(int) int
	dfs = func(eid int) int {
		employee := employeeMap[eid]
		total := employee.Importance
		for _, subId := range employee.Subordinates {
			total += dfs(subId)
		}
		return total
	}
	return dfs(id)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var employees []*Employee
	var id int

	var employeesJson [][]interface{}
	if err := json.Unmarshal([]byte(inputValues[0]), &employeesJson); err != nil {
		log.Fatal(err)
	}
	for _, employeeJson := range employeesJson {
		eid := int(employeeJson[0].(float64))
		importance := int(employeeJson[1].(float64))
		subordinates := []int{}
		for _, sub := range employeeJson[2].([]interface{}) {
			subordinates = append(subordinates, int(sub.(float64)))
		}
		employees = append(employees, &Employee{
			Id:           eid,
			Importance:   importance,
			Subordinates: subordinates,
		})
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &id); err != nil {
		log.Fatal(err)
	}

	return getImportance(employees, id)
}

// Employee Definition for Employee.
type Employee struct {
	Id           int
	Importance   int
	Subordinates []int
}
