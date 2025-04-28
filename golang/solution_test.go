package golang

import (
	problem "leetCode/problems/problems_344"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "344", "problems", problem.Solve)
}
