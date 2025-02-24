package problem2502

import (
	"encoding/json"
	"log"
	"strings"
)

type Allocator struct {
    
}


func Constructor(n int) Allocator {
    
}


func (this *Allocator) Allocate(size int, mID int) int {
    
}


func (this *Allocator) FreeMemory(mID int) int {
    
}


/**
 * Your Allocator object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Allocate(size,mID);
 * param_2 := obj.FreeMemory(mID);
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
	obj := Constructor(int(opValues[0][0].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "allocate", "Allocate":
			res = obj.Allocate(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "freeMemory", "FreeMemory":
			res = obj.FreeMemory(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
