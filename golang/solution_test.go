package golang

import (
	problem "leetCode/problems/problems_63"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "63", "problems", problem.Solve)
}
