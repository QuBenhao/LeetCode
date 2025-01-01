package golang

import (
	problem "leetCode/problems/problems_729"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "729", "problems", problem.Solve)
}
