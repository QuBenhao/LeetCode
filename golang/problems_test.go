package golang

import (
	"leetCode/problems/problems_102"
	"leetCode/problems/problems_34"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "102", "problems", problem102.Solve)
	TestEach(t, "34", "problems", problem34.Solve)
}
