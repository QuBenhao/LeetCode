package golang

import (
	problem "leetCode/problems/problems_36"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "36", "problems", problem.Solve)
}
