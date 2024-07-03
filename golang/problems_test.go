package golang

import (
	"leetCode/problems/problems_560"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "560", "problems", problem560.Solve)
}
