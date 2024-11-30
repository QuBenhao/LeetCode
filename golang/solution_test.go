package golang

import (
	problem "leetCode/problems/problems_51"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "51", "problems", problem.Solve)
}
