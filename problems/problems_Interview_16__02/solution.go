package problemInterview_16__02

import (
	"encoding/json"
	"log"
	"strings"
)

type WordsFrequency struct {
    
}


func Constructor(book []string) WordsFrequency {
    
}


func (this *WordsFrequency) Get(word string) int {
    
}


/**
 * Your WordsFrequency object will be instantiated and called as such:
 * obj := Constructor(book);
 * param_1 := obj.Get(word);
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
	var bookArr []string
	if v, ok := opValues[0][0].([]string); ok {
		bookArr = v
	} else {
		for _, vi := range opValues[0][0].([]any) {
			bookArr = append(bookArr, vi.(string))
		}
	}
	obj := Constructor(bookArr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "get", "Get":
			res = obj.Get(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
