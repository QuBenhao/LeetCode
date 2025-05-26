package golang

import (
	"leetCode/problems/problems_LCR_006"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_006", "problems", problemLCR_006.Solve)
}
