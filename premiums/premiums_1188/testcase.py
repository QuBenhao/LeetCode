from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, ['BoundedBlockingQueue', 'enqueue', 'dequeue', 'dequeue', 'enqueue', 'enqueue', 'enqueue', 'enqueue', 'dequeue'], [[2], [1], [], [], [0], [2], [3], [4], []]], Output=[1, 0, 2, 2]))
		self.testcases.append(case(Input=[3, 4, ['BoundedBlockingQueue', 'enqueue', 'enqueue', 'enqueue', 'dequeue', 'dequeue', 'dequeue', 'enqueue'], [[3], [1], [0], [2], [], [], [], [3]]], Output=[1, 0, 2, 1]))

	def get_testcases(self):
		return self.testcases
