package problem2296

import (
	"encoding/json"
	"log"
	"strings"
)

type TextEditor struct {
    
}


func Constructor() TextEditor {
    
}


func (this *TextEditor) AddText(text string)  {
    
}


func (this *TextEditor) DeleteText(k int) int {
    
}


func (this *TextEditor) CursorLeft(k int) string {
    
}


func (this *TextEditor) CursorRight(k int) string {
    
}


/**
 * Your TextEditor object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddText(text);
 * param_2 := obj.DeleteText(k);
 * param_3 := obj.CursorLeft(k);
 * param_4 := obj.CursorRight(k);
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
		case "addText", "AddText":
			res = nil
			obj.AddText(opValues[i][0].(string))
		case "deleteText", "DeleteText":
			res = obj.DeleteText(int(opValues[i][0].(float64)))
		case "cursorLeft", "CursorLeft":
			res = obj.CursorLeft(int(opValues[i][0].(float64)))
		case "cursorRight", "CursorRight":
			res = obj.CursorRight(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
