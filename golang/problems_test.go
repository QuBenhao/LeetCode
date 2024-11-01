package golang

import (
	"leetCode/problems/problems_LCR_011"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_011", "problems", problemLCR_011.Solve)
}
