package golang

import (
	"leetCode/problems/problems_LCR_024"
	"leetCode/problems/problems_LCR_109"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_024", "problems", problemLCR_024.Solve)
	TestEach(t, "LCR_109", "problems", problemLCR_109.Solve)
}
