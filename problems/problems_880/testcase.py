from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("leet2code3", 10), Output="o"))
        self.testcases.append(case(Input=("ha22", 5), Output="h"))
        self.testcases.append(case(Input=("a23", 6), Output="a"))
        self.testcases.append(case(Input=("a2345678999999999999999", 1), Output="a"))
        self.testcases.append(case(Input=("y959q969u3hb22odq595", 222280369), Output="y"))
        self.testcases.append(case(Input=("cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imn"
                                          "cfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg",480551547),
                                   Output="x"))

    def get_testcases(self):
        return self.testcases
