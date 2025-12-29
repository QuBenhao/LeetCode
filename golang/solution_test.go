package golang

import (
	problem "leetCode/problems/problems_840"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "840", "problems", problem.Solve)
}
