package golang

import (
	"leetCode/problems/problems_3597"
	"leetCode/problems/problems_3598"
	"leetCode/problems/problems_3599"
	"leetCode/problems/problems_3600"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3597", "problems", problem3597.Solve)
	TestEach(t, "3598", "problems", problem3598.Solve)
	TestEach(t, "3599", "problems", problem3599.Solve)
	TestEach(t, "3600", "problems", problem3600.Solve)
}
