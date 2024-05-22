//
// Created by 曲本豪 on 2024/5/21.
//

#include "TestMain.h"
#include "Solution.h"

using namespace std;
using json = nlohmann::json;

// Demonstrate some basic assertions.
TEST(HelloTest, BasicAssertions) {
    // Expect two strings not to be equal.
    EXPECT_STRNE("hello", "world");
    // Expect equality.
    EXPECT_EQ(7 * 6, 42);
}

namespace LeetCode {
    namespace qubh {
        TEST(SolutionTest, TwoSum) {
            Solution solution;
            vector<int> nums = {2, 7, 11, 15};
            int target = 9;
            vector<int> expected = {0, 1};
            EXPECT_EQ(solution.Solve("[2,7,11,15]\n9"), json::parse(expected));
        }
    } // qubh
} // LeetCode

int main(int argc, char **argv) {

    // Run the tests.
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}