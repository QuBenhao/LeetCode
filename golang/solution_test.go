package golang

import (
	problem "leetCode/problems/problems_61"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "61", "problems", problem.Solve)
}
