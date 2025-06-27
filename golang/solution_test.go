package golang

import (
	problem "leetCode/problems/problems_228"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "228", "problems", problem.Solve)
}
