package golang

import (
	"leetCode/problems/problems_131"
	"leetCode/problems/problems_LCR_008"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_008", "problems", problemLCR_008.Solve)
	TestEach(t, "131", "problems", problem131.Solve)
}
