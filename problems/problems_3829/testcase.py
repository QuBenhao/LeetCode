from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['RideSharingSystem', 'addRider', 'addDriver', 'addRider', 'matchDriverWithRider', 'addDriver', 'cancelRider', 'matchDriverWithRider', 'matchDriverWithRider'], [[], [3], [2], [1], [], [5], [3], [], []]], Output=[None, None, None, None, [2, 3], None, None, [5, 1], [-1, -1]]))
		self.testcases.append(case(Input=[['RideSharingSystem', 'addRider', 'addDriver', 'addDriver', 'matchDriverWithRider', 'addRider', 'cancelRider', 'matchDriverWithRider'], [[], [8], [8], [6], [], [2], [2], []]], Output=[None, None, None, None, [8, 8], None, None, [-1, -1]]))
		self.testcases.append(case(Input=[["RideSharingSystem","addDriver","cancelRider","addRider","matchDriverWithRider"],[[],[2],[1],[1],[]]], Output=[None,None,None,None,[2,1]]))

	def get_testcases(self):
		return self.testcases
