package golang

import (
	problem "leetCode/problems/problems_946"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "946", "problems", problem.Solve)
}
