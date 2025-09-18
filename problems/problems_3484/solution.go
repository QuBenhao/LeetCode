package problem3484

import (
	"encoding/json"
	"log"
	"strings"
)

type Spreadsheet struct {
    
}


func Constructor(rows int) Spreadsheet {
    
}


func (this *Spreadsheet) SetCell(cell string, value int)  {
    
}


func (this *Spreadsheet) ResetCell(cell string)  {
    
}


func (this *Spreadsheet) GetValue(formula string) int {
    
}


/**
 * Your Spreadsheet object will be instantiated and called as such:
 * obj := Constructor(rows);
 * obj.SetCell(cell,value);
 * obj.ResetCell(cell);
 * param_3 := obj.GetValue(formula);
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
		case "setCell", "SetCell":
			res = nil
			obj.SetCell(opValues[i][0].(string), int(opValues[i][1].(float64)))
		case "resetCell", "ResetCell":
			res = nil
			obj.ResetCell(opValues[i][0].(string))
		case "getValue", "GetValue":
			res = obj.GetValue(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
