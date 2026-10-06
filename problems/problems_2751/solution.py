import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.survivedRobotsHealths(*test_input)

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Robot indices sorted by position
        sorted_indices = sorted(range(len(positions)), key=lambda i: positions[i])

        survivors = {}  # {original index: final health}
        right_going = []  # Stack: [health, original index]

        for i in sorted_indices:
            h, d = healths[i], directions[i]

            if d == 'R':
                right_going.append([h, i])
            else:  # Moving left: collide with right-moving robots on the stack
                while right_going and h > 0:
                    top_h, top_i = right_going[-1]

                    if top_h > h:
                        right_going[-1][0] -= 1
                        h = 0
                    elif top_h < h:
                        right_going.pop()
                        h -= 1
                    else:
                        right_going.pop()
                        h = 0

                if h > 0:
                    survivors[i] = h

        # Right-moving robots remaining on the stack
        for h, i in right_going:
            survivors[i] = h

        # Return results in original index order
        return [survivors[i] for i in sorted(survivors.keys())]

