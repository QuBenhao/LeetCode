package problem155

import (
	"encoding/json"
	"log"
	"strings"
)

type MinStack struct {

}


func Constructor() MinStack {

}


func (this *MinStack) Push(val int)  {

}


func (this *MinStack) Pop()  {

}


func (this *MinStack) Top() int {

}


func (this *MinStack) GetMin() int {

}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]interface{}
	var ans []interface{}
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj :=Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "push", "Push":
			res = nil
			obj.Push(int(opValues[i][0].(float64)))
		case "pop", "Pop":
			res = nil
			obj.Pop()
		case "top", "Top":
			res = obj.Top()
		case "getMin", "GetMin":
			res = obj.GetMin()
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
