package golang

import (
	problem "leetCode/problems/problems_3000"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3000", "problems", problem.Solve)
}
