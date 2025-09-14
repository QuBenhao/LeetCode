package golang

import (
	problem3678 "leetCode/problems/problems_3678"
	problem3679 "leetCode/problems/problems_3679"
	problem3681 "leetCode/problems/problems_3681"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3678", "problems", problem3678.Solve)
	TestEach(t, "3679", "problems", problem3679.Solve)
	TestEach(t, "3681", "problems", problem3681.Solve)
}
