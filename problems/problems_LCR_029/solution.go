package problemLCR_029

import (
	"encoding/json"
	"log"
	"strings"
)

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 * }
 */

func insert(aNode *Node, x int) *Node {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var aNode *Node
	var x int

	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}

	return FIXME(insert(aNode, x))
}
