package golang

import (
	"leetCode/problems/problems_LCR_003"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_003", "problems", problemLCR_003.Solve)
}
