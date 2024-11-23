package golang

import (
	"leetCode/problems/problems_LCR_004"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_004", "problems", problemLCR_004.Solve)
}
