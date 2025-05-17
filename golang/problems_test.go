package golang

import (
	"leetCode/problems/problems_LCR_013"
	"leetCode/problems/problems_LCR_067"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_067", "problems", problemLCR_067.Solve)
	TestEach(t, "LCR_013", "problems", problemLCR_013.Solve)
}
