package golang

import (
	problem "leetCode/problems/problems_132"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "132", "problems", problem.Solve)
}
