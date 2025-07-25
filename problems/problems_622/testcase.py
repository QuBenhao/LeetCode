from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MyCircularQueue', 'enQueue', 'enQueue', 'enQueue', 'enQueue', 'Rear', 'isFull', 'deQueue', 'enQueue', 'Rear'], [[3], [1], [2], [3], [4], [], [], [], [4], []]], Output=[None, True, True, True, False, 3, True, True, True, 4]))

	def get_testcases(self):
		return self.testcases
