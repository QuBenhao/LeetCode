package problem3508

import (
	"encoding/json"
	"log"
	"strings"
)

type Router struct {
    
}


func Constructor(memoryLimit int) Router {
    
}


func (this *Router) AddPacket(source int, destination int, timestamp int) bool {
    
}


func (this *Router) ForwardPacket() []int {
    
}


func (this *Router) GetCount(destination int, startTime int, endTime int) int {
    
}


/**
 * Your Router object will be instantiated and called as such:
 * obj := Constructor(memoryLimit);
 * param_1 := obj.AddPacket(source,destination,timestamp);
 * param_2 := obj.ForwardPacket();
 * param_3 := obj.GetCount(destination,startTime,endTime);
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
	obj := Constructor(int(opValues[0][0].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "addPacket", "AddPacket":
			res = obj.AddPacket(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)))
		case "forwardPacket", "ForwardPacket":
			res = obj.ForwardPacket()
		case "getCount", "GetCount":
			res = obj.GetCount(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
