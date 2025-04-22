package golang

import (
	"leetCode/problems/problems_LCR_045"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_045", "problems", problemLCR_045.Solve)
}
