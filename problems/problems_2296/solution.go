package problem2296

import (
	"encoding/json"
	"log"
	"strings"
)

type TextEditor struct {
	left, right []byte
}

func Constructor() TextEditor {
	return TextEditor{}
}

func (textEditor *TextEditor) AddText(text string) {
	textEditor.left = append(textEditor.left, text...)
}

func (textEditor *TextEditor) DeleteText(k int) int {
	k = min(k, len(textEditor.left))
	textEditor.left = textEditor.left[:len(textEditor.left)-k]
	return k
}

func (textEditor *TextEditor) CursorLeft(k int) string {
	for k > 0 && len(textEditor.left) > 0 {
		textEditor.right = append(textEditor.right, textEditor.left[len(textEditor.left)-1])
		textEditor.left = textEditor.left[:len(textEditor.left)-1]
		k--
	}
	return string(textEditor.left[max(0, len(textEditor.left)-10):])
}

func (textEditor *TextEditor) CursorRight(k int) string {
	for k > 0 && len(textEditor.right) > 0 {
		textEditor.left = append(textEditor.left, textEditor.right[len(textEditor.right)-1])
		textEditor.right = textEditor.right[:len(textEditor.right)-1]
		k--
	}
	return string(textEditor.left[max(0, len(textEditor.left)-10):])
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddText(text);
 * param_2 := obj.DeleteText(k);
 * param_3 := obj.CursorLeft(k);
 * param_4 := obj.CursorRight(k);
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
