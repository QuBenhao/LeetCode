package golang

import (
	problem "leetCode/problems/problems_2048"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "2048", "problems", problem.Solve)
}
