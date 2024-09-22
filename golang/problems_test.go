package golang

import (
	"leetCode/problems/problems_LCR_010"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_010", "problems", problemLCR_010.Solve)
}
