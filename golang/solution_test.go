package golang

import (
	problem "leetCode/problems/problems_22"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "22", "problems", problem.Solve)
}
