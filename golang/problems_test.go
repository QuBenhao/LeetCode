package golang

import (
	"leetCode/problems/problems_1143"
	"leetCode/problems/problems_31"
	"leetCode/problems/problems_LCR_014"
	"leetCode/problems/problems_LCR_036"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "1143", "problems", problem1143.Solve)
	TestEach(t, "31", "problems", problem31.Solve)
	TestEach(t, "LCR_014", "problems", problemLCR_014.Solve)
	TestEach(t, "LCR_036", "problems", problemLCR_036.Solve)
}
