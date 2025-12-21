package golang

import (
	problem "leetCode/problems/problems_960"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "960", "problems", problem.Solve)
}
