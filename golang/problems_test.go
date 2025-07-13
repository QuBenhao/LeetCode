package golang

import (
	problem3612 "leetCode/problems/problems_3612"
	problem3613 "leetCode/problems/problems_3613"
	problem3614 "leetCode/problems/problems_3614"
	problem3615 "leetCode/problems/problems_3615"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3612", "problems", problem3612.Solve)
	TestEach(t, "3613", "problems", problem3613.Solve)
	TestEach(t, "3614", "problems", problem3614.Solve)
	TestEach(t, "3615", "problems", problem3615.Solve)
}
