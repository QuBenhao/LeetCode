package problemLCR_058

import (
	"encoding/json"
	"log"
	"strings"
)

type MyCalendar struct {

}


func Constructor() MyCalendar {

}


func (this *MyCalendar) Book(start int, end int) bool {

}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
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
		case "book", "Book":
			res = obj.Book(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
