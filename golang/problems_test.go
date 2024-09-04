package golang

import (
	"leetCode/problems/problems_23"
	"leetCode/problems/problems_LCR_092"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_092", "problems", problemLCR_092.Solve)
	TestEach(t, "23", "problems", problem23.Solve)
}
