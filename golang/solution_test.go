package golang

import (
	problem "leetCode/problems/problems_1415"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1415", "problems", problem.Solve)
}
