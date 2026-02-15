package golang

import (
	problem "leetCode/problems/problems_190"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "190", "problems", problem.Solve)
}
