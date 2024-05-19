from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]], ['ATL', 'PEK', 'LAX', 'DXB', 'HND'], ['ATL', 'DXB', 'HND', 'LAX']], Output=[0, 2, 4, 2]))
		self.testcases.append(case(Input=[4, [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]], ['ATL', 'PEK', 'LAX', 'DXB'], ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX']], Output=[0, 1, 0, 1, 0, 1, 0, 1]))
		self.testcases.append(case(Input=[6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], ['ATL', 'PEK', 'LAX', 'ATL', 'DXB', 'HND'], ['ATL', 'DXB', 'HND', 'DXB', 'ATL', 'LAX', 'PEK']], Output=[3, 4, 5, 4, 3, 2, 1]))

	def get_testcases(self):
		return self.testcases
