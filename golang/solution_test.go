package golang

import (
	problem "leetCode/problems/problems_120"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "120", "problems", problem.Solve)
}
