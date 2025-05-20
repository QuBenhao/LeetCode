package test

import (
	"encoding/json"
	"fmt"
	"log"
	"testing"

	"github.com/stretchr/testify/assert"

	. "leetCode/golang/tree_next"
)

func TestTreeNodeNext(t *testing.T) {
	inputStr := "[1,2,3,4,5,null,7]"
	node := ArrayToTreeNext(inputStr)
	assert.Equal(t, 1, node.Val)
	assert.Equal(t, 2, node.Left.Val)
	assert.Equal(t, 3, node.Right.Val)

	node.Left.Next = node.Right
	node.Left.Left.Next = node.Left.Right
	node.Left.Right.Next = node.Right.Right
	var input []any
	if err := json.Unmarshal([]byte("[1, null, 2, 3, null, 4, 5, 7, null]"), &input); err != nil {
		log.Fatal(err)
	}
	assert.Equal(t, fmt.Sprintf("%v", input), fmt.Sprintf("%v", TreeNextToArray(node)))
}
