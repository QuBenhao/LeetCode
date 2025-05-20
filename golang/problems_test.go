package golang

import (
	"leetCode/problems/problems_LCR_103"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_103", "problems", problemLCR_103.Solve)
}
