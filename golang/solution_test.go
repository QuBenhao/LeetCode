package golang

import (
	problem "leetCode/problems/problems_552"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "552", "problems", problem.Solve)
}
