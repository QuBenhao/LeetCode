package golang

import (
	"leetCode/problems/problems_LCR_099"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_099", "problems", problemLCR_099.Solve)
}
