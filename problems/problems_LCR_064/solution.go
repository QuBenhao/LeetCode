package problemLCR_064

import (
	"encoding/json"
	"log"
	"strings"
)

type MagicDictionary struct {

}


/** Initialize your data structure here. */
func Constructor() MagicDictionary {

}


func (this *MagicDictionary) BuildDict(dictionary []string)  {

}


func (this *MagicDictionary) Search(searchWord string) bool {

}


/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dictionary);
 * param_2 := obj.Search(searchWord);
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
		case "buildDict", "BuildDict":
			var arr []string
			if v, ok := opValues[i][0].([]string); ok {
				arr = v
			} else {
				for _, vi := range opValues[i][0].([]interface{}) {
					arr = append(arr, vi.(string))
				}
			}
			res = nil
			obj.BuildDict(arr)
		case "search", "Search":
			res = obj.Search(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
