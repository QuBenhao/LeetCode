package golang

import (
	problem "leetCode/problems/problems_3270"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3270", "problems", problem.Solve)
}
