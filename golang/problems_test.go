package golang

import (
	"leetCode/problems/problems_994"
	"leetCode/problems/problems_121"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "994", "problems", problem994.Solve)
	TestEach(t, "121", "problems", problem121.Solve)
}
