package golang

import (
	"leetCode/problems/problems_236"
	"leetCode/problems/problems_LCR_106"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_106", "problems", problemLCR_106.Solve)
	TestEach(t, "236", "problems", problem236.Solve)
}
