package golang

import (
	"leetCode/problems/problems_LCR_078"
	"leetCode/problems/problems_LCR_117"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_117", "problems", problemLCR_117.Solve)
	TestEach(t, "LCR_078", "problems", problemLCR_078.Solve)
}
