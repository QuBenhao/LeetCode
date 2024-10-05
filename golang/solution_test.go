package golang

import (
	problem "leetCode/problems/problems_134"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "134", "problems", problem.Solve)
}
