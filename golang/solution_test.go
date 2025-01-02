package golang

import (
	problem "leetCode/problems/problems_731"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "731", "problems", problem.Solve)
}
