package problem1206

import (
	"encoding/json"
	"log"
	"strings"
)

type Skiplist struct {
    
}


func Constructor() Skiplist {
    
}


func (this *Skiplist) Search(target int) bool {
    
}


func (this *Skiplist) Add(num int)  {
    
}


func (this *Skiplist) Erase(num int) bool {
    
}


/**
 * Your Skiplist object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Search(target);
 * obj.Add(num);
 * param_3 := obj.Erase(num);
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
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "search", "Search":
			res = obj.Search(int(opValues[i][0].(float64)))
		case "add", "Add":
			res = nil
			obj.Add(int(opValues[i][0].(float64)))
		case "erase", "Erase":
			res = obj.Erase(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
