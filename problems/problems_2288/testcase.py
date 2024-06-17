from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['there are $1 $2 and 5$ candies in the shop', 50], Output="there are $0.50 $1.00 and 5$ candies in the shop"))
		self.testcases.append(case(Input=['1 2 $3 4 $5 $6 7 8$ $9 $10$', 100], Output="1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"))

	def get_testcases(self):
		return self.testcases
