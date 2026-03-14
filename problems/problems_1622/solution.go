package problem1622

import (
	"encoding/json"
	"log"
	"strings"
)

type Fancy struct {
    
}


func Constructor() Fancy {
    
}


func (this *Fancy) Append(val int)  {
    
}


func (this *Fancy) AddAll(inc int)  {
    
}


func (this *Fancy) MultAll(m int)  {
    
}


func (this *Fancy) GetIndex(idx int) int {
    
}


/**
 * Your Fancy object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Append(val);
 * obj.AddAll(inc);
 * obj.MultAll(m);
 * param_4 := obj.GetIndex(idx);
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
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "append", "Append":
			res = nil
			obj.Append(int(opValues[i][0].(float64)))
		case "addAll", "AddAll":
			res = nil
			obj.AddAll(int(opValues[i][0].(float64)))
		case "multAll", "MultAll":
			res = nil
			obj.MultAll(int(opValues[i][0].(float64)))
		case "getIndex", "GetIndex":
			res = obj.GetIndex(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
