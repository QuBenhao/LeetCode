package golang

import (
	problem "leetCode/problems/problems_862"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "862", "problems", problem.Solve)
}
