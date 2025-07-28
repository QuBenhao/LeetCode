package golang

import (
	problem "leetCode/problems/problems_741"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "741", "problems", problem.Solve)
}
