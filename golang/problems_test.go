package golang

import (
	"leetCode/problems/problems_LCR_058"
	"leetCode/problems/problems_LCR_104"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_058", "problems", problemLCR_058.Solve)
	TestEach(t, "LCR_104", "problems", problemLCR_104.Solve)
}
