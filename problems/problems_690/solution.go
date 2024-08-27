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

	var employees_input_array []interface{}
	if err := json.Unmarshal([]byte(inputValues[0]), &employees_input_array); err != nil {
		log.Fatal(err)
	}
	for _, ipt := range employees_input_array {
		employees = append(employees, constructor(ipt))
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &id); err != nil {
		log.Fatal(err)
	}

	return getImportance(employees, id)
}

// Definition for Employee.
type Employee struct {
	Id           int
	Importance   int
	Subordinates []int
}

func constructor(input interface{}) *Employee {
	arr := input.([]interface{})
	num_arr := arr[2].([]interface{})
	nums := make([]int, len(num_arr))
	for i, v := range num_arr {
		nums[i] = int(v.(float64))
	}
	return &Employee{int(arr[0].(float64)), int(arr[1].(float64)), nums}
}
