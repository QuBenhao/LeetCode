package golang

import (
	"leetCode/problems/problems_239"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "239", "problems", problem239.Solve)
}
