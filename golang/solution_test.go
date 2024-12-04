package golang

import (
	problem "leetCode/problems/problems_3001"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3001", "problems", problem.Solve)
}
