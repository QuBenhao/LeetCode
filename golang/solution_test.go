package golang

import (
	problem "leetCode/problems/problems_661"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "661", "problems", problem.Solve)
}
