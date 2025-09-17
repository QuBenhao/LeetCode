package problem3408

import (
	"encoding/json"
	"log"
	"strings"
)

type TaskManager struct {
    
}


func Constructor(tasks [][]int) TaskManager {
    
}


func (this *TaskManager) Add(userId int, taskId int, priority int)  {
    
}


func (this *TaskManager) Edit(taskId int, newPriority int)  {
    
}


func (this *TaskManager) Rmv(taskId int)  {
    
}


func (this *TaskManager) ExecTop() int {
    
}


/**
 * Your TaskManager object will be instantiated and called as such:
 * obj := Constructor(tasks);
 * obj.Add(userId,taskId,priority);
 * obj.Edit(taskId,newPriority);
 * obj.Rmv(taskId);
 * param_4 := obj.ExecTop();
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	var tasksArr [][]int
	if v, ok := opValues[0][0].([][]int); ok {
		tasksArr = v
	} else {
		tasksArr = make([][]int, len(opValues[0][0].([]any)))
		for i := range tasksArr {
			tasksArr[i] = make([]int, len(opValues[0][0].([]any)[i].([]any)))
			for j := range tasksArr[i] {
				tasksArr[i][j] = int(opValues[0][0].([]any)[i].([]any)[j].(float64))
			}
		}
	}
	obj := Constructor(tasksArr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "add", "Add":
			res = nil
			obj.Add(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)))
		case "edit", "Edit":
			res = nil
			obj.Edit(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "rmv", "Rmv":
			res = nil
			obj.Rmv(int(opValues[i][0].(float64)))
		case "execTop", "ExecTop":
			res = obj.ExecTop()
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
