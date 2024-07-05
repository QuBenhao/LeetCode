package golang

import (
	problem "leetCode/problems/problems_3101"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3101", "problems", problem.Solve)
}
