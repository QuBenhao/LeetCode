package golang

import (
	problem "leetCode/problems/problems_788"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "788", "problems", problem.Solve)
}
