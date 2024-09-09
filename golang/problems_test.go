package golang

import (
	"leetCode/problems/problems_LCR_002"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_002", "problems", problemLCR_002.Solve)
}
