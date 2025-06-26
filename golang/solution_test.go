package golang

import (
	problem "leetCode/problems/problems_799"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "799", "problems", problem.Solve)
}
