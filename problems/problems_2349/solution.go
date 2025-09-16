package problem2349

import (
	"encoding/json"
	"log"
	"strings"
)

type NumberContainers struct {
    
}


func Constructor() NumberContainers {
    
}


func (this *NumberContainers) Change(index int, number int)  {
    
}


func (this *NumberContainers) Find(number int) int {
    
}


/**
 * Your NumberContainers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Change(index,number);
 * param_2 := obj.Find(number);
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
		case "change", "Change":
			res = nil
			obj.Change(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "find", "Find":
			res = obj.Find(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
