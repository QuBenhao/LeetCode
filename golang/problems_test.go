package golang

import (
	"leetCode/problems/problems_98"
	"leetCode/problems/problems_33"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "98", "problems", problem98.Solve)
	TestEach(t, "33", "problems", problem33.Solve)
}
