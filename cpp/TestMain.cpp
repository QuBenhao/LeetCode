//
// Created by 曲本豪 on 2024/5/21.
//

#include "TestMain.h"
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

namespace LeetCode {
    namespace qubh {
        TEST(SolutionTest, TwoSum) {
            vector<int> nums = {2, 7, 11, 15};
            int target = 9;
            vector<int> expected = {0, 1};
            EXPECT_EQ(leetcode::qubh::Solve("[2,7,11,15]\n9"), json(expected));
        }
    } // qubh
} // LeetCode

int main(int argc, char **argv) {

    // Run the tests.
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}