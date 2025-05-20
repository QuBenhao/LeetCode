package test

import (
	. "leetCode/golang/double_linked_node_child"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDoubleListNode(t *testing.T) {
	arr := []any{1, 2, 3, 4, 5, 6, nil, nil, nil, 7, 8, 9, 10, nil, nil, 11, 12}
	node := IntArrayToDoubleLinkedNode(arr)
	i := 0
	for tmp := node; tmp != nil; tmp = tmp.Next {
		if i == 2 {
			assert.NotNil(t, tmp.Child)
			assert.Equal(t, 7, tmp.Child.Val)
		}
		assert.Equal(t, arr[i], tmp.Val)
		i++
	}
	assert.Equal(t, arr, DoubleLinkedNodeToIntArray(node))

}
