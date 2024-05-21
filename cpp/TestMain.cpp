//
// Created by 曲本豪 on 2024/5/21.
//

#include "TestMain.h"

// Demonstrate some basic assertions.
TEST(HelloTest, BasicAssertions) {
    // Expect two strings not to be equal.
    EXPECT_STRNE("hello", "world");
    // Expect equality.
    EXPECT_EQ(7 * 6, 42);
}

namespace LeetCode {
    namespace qubh {

    } // qubh
} // LeetCode