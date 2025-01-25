package golang

import (
	problem "leetCode/problems/problems_40"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "40", "problems", problem.Solve)
}
