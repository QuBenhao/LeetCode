package golang

import (
	problem "leetCode/problems/problems_315"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "315", "problems", problem.Solve)
}
