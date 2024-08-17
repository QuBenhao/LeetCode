package problemLCR_062

import (
	"encoding/json"
	"log"
	"strings"
)

type Trie struct {

}


/** Initialize your data structure here. */
func Constructor() Trie {

}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {

}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {

}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {

}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
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
		case "insert", "Insert":
			res = nil
			obj.Insert(opValues[i][0].(string))
		case "search", "Search":
			res = obj.Search(opValues[i][0].(string))
		case "startsWith", "StartsWith":
			res = obj.StartsWith(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
