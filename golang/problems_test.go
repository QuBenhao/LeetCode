package golang

import (
	"leetCode/problems/problems_56"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "56", "problems", problem56.Solve)
}
