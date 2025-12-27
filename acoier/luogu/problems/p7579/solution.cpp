//
// Created by benhao on 2025/12/26.
//

#include <iostream>
#include <algorithm>
#include <stdexcept>

using namespace std;

int n;
int x, y;

int ask_size(int l1, int r1, int l2, int r2) {
    cout << 1 << " "  << r1 - l1 << " ";
    for (int i = l1; i < r1; ++i) {
        cout << i << " ";
    }
    cout << r2 - l2 << " ";
    for (int i = l2; i < r2 - 1; ++i) {
        cout << i << " ";
    }
    cout << r2 - 1 << endl;
    char c;
    cin >> c;
    if (c == '=') {
        return 0;
    }
    return c == '<' ? -1 : 1;
}

void helper(int l, int r, int remain) {
    if (l == r) {
        if (x == -1) {
            x = l;
        } else {
            y = l;
        }
        return;
    }
    if (remain == 0) {
        return;
    }
    int num = r - l + 1;
    int d = num / 3, m = num % 3;
    if (d == 0) {
        if (remain == 2) {
            x = l;
            y = r;
        } else {
            int diff = ask_size(l, l+1, r, r+1);
            if (diff < 0) {
                if (x == -1) {
                    x = l;
                } else {
                    y = l;
                }
            } else {
                if (x == -1) {
                    x = r;
                } else {
                    y = r;
                }
            }
        }
        return;
    }
    int lmid = l + d, rmid = l + d * 2;
    int d1 = ask_size(l, lmid, lmid, rmid);
    // int d2 = ask_size(lmid, rmid, rmid, rmid + d);
    // d1: -1, 0, 1; d2: -1, 0, 1
    if (d1 == -1) {
        // 1 < 2, 2里没有坏球
        if (remain == 1) {
            helper(l, lmid-1, remain);
            return;
        }
        // 2中没有目标
        if (m == 2) {
            int d2 = ask_size(lmid, rmid + 1, rmid + 1, r+1);
            if (d2 == -1) {
                // 2 < 3, 说明rmid为坏球
                if (x == -1) {
                    x = rmid;
                } else {
                    y = rmid;
                }
                --remain;
                helper(l, lmid - 1, remain);
            } else if (d2 == 1) {
                // 2 > 3, 说明坏球在rmid+1~r
                helper(l, lmid - 1, 1);
                helper(rmid + 1, r, 1);
            } else {
                // 说明2/3里没有坏球
                helper(l, lmid - 1, remain);
            }
        } else if (m == 0) {
            int d2 = ask_size(lmid, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3, 不可能发生
                throw invalid_argument("不可能发生依次变大");
            }
            if (d2 == 1) {
                // 2 > 3
                helper(l, lmid - 1, 1);
                helper(rmid, r, 1);
            } else {
                // 2 == 3, 说明2/3里没有坏球
                helper(l, lmid - 1, remain);
            }
        } else {
            int d2 = ask_size(lmid-1, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3, 说明lmid-1为坏球
                if (x == -1) {
                    x = lmid - 1;
                } else {
                    y = lmid - 1;
                }
                helper(l, lmid - 2, 1);
            } else if (d2 == 1) {
                // 2 > 3
                helper(l, lmid - 2, 1);
                helper(rmid, r, 1);
            } else {
                helper(l, lmid - 2, remain);
            }
        }
    } else if (d1 == 0) {
        // 1 == 2
        if (remain == 1) {
            helper(rmid, r, remain);
            return;
        }
        if (m == 2) {
            int d2 = ask_size(lmid, rmid + 1, rmid + 1, r+1);
            if (d2 == -1) {
                // 2 < 3, 说明3里面没有坏球, 且rmid不是坏球
                helper(l, lmid - 1, 1);
                helper(lmid, rmid - 1, 1);
            } else if (d2 == 1) {
                // 2 > 3, 说明坏球在rmid+1~r
                helper(rmid + 1, r, remain);
            } else {
                // 说明rmid是坏球, rmid+1~r有一个坏球
                if (x == -1) {
                    x = rmid;
                } else {
                    y = rmid;
                }
                helper(rmid+1, r, 1);
            }
        } else if (m == 0) {
            int d2 = ask_size(lmid, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3, 1、2各一个坏球
                helper(l, lmid - 1, 1);
                helper(lmid, rmid - 1, 1);
            } else if (d2 == 1) {
                // 2 > 3
                helper(rmid, r, remain);
            } else {
                // 2 == 3, 不可能发生
                throw invalid_argument("不可能发生都相等");
            }
        } else {
            int d2 = ask_size(lmid-1, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3, 说明1, 2各一个坏球
                helper(l, lmid - 1, 1);
                helper(lmid, rmid - 1, 1);
            } else if (d2 == 1) {
                // 2 > 3, 说明1, 2没有坏球
                helper(rmid, r, remain);
            } else {
                // 2 == 3
                throw invalid_argument("不可能发生都相等");
            }
        }
    } else {
        // 1 > 2, 1里没有坏球, 2里至少一个坏球
        if (remain == 1) {
            helper(lmid, rmid - 1, remain);
            return;
        }
        if (m == 2) {
            int d2 = ask_size(lmid, rmid+1, rmid+1, r+1);
            if (d2 == -1) {
                // 2 < 3, 说明3里没有坏球
                helper(lmid, rmid, remain);
            } else if (d2 == 1) {
                // 2 > 3
                throw invalid_argument("不可能依次变小");
            } else {
                // 2 == 3
                helper(lmid, rmid - 1, 1);
                helper(rmid + 1, r, 1);
            }
        } else if (m == 0) {
            int d2 = ask_size(lmid, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3
                helper(lmid, rmid - 1, remain);
            } else if (d2 == 1) {
                // 2 > 3
                throw invalid_argument("不可能依次变小");
            } else {
                // 2 == 3, 说明2/3里各一个坏球
                helper(lmid, rmid - 1, 1);
                helper(rmid, r, 1);
            }
        } else {
            int d2 = ask_size(lmid-1, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3
                helper(lmid, rmid - 1, remain);
            } else if (d2 == 1) {
                // 2 > 3
                throw invalid_argument("不可能依次变小");
            } else {
                helper(lmid, rmid - 1, 1);
                helper(rmid, r, 1);
            }
        }
    }
}

int main() {
    cin >> n;
    x = -1; y = -1;
    helper(1, n, 2);
    cout << 2 << " " << min(x, y) << " " << max(x, y) << endl;
}