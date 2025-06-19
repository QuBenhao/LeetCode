package golang

import (
	problem "leetCode/problems/problems_775"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "775", "problems", problem.Solve)
}
