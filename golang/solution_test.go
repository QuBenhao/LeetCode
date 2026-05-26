package golang

import (
	problem "leetCode/problems/problems_3121"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3121", "problems", problem.Solve)
}
