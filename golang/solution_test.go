package golang

import (
	problem "leetCode/problems/problems_640"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "640", "problems", problem.Solve)
}
