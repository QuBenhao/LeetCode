package golang

import (
	"leetCode/problems/problems_LCR_100"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_100", "problems", problemLCR_100.Solve)
}
