import optparse
import sys


def readCommand(argv):
    parser = optparse.OptionParser(
        description='Run tests on leetcode')
    parser.set_defaults(generateSolutions=False, edxOutput=False, gsOutput=False,
                        muteOutput=False, printTestCase=False, noGraphics=False)
    # parser.add_option('--test-directory',
    #                   dest='testRoot',
    #                   default='test_cases',
    #                   help='Root test directory which contains subdirectories corresponding to each question')
    (options, args) = parser.parse_args(argv)
    return options


if __name__ == "__main__":
    readCommand(sys.argv)
