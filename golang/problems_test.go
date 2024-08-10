package golang

import (
	"leetCode/problems/problems_19"
	"leetCode/problems/problems_230"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "19", "problems", problem19.Solve)
	TestEach(t, "230", "problems", problem230.Solve)
}
