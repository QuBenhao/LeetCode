package golang

import (
	problem "leetCode/problems/problems_453"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "453", "problems", problem.Solve)
}
