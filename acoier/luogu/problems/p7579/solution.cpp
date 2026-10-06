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
        // 1 < 2: group 2 contains no defective balls
        if (remain == 1) {
            helper(l, lmid-1, remain);
            return;
        }
        // Group 2 contains no target
        if (m == 2) {
            int d2 = ask_size(lmid, rmid + 1, rmid + 1, r+1);
            if (d2 == -1) {
                // 2 < 3: rmid is a defective ball
                if (x == -1) {
                    x = rmid;
                } else {
                    y = rmid;
                }
                --remain;
                helper(l, lmid - 1, remain);
            } else if (d2 == 1) {
                // 2 > 3: the defective ball is in rmid+1~r
                helper(l, lmid - 1, 1);
                helper(rmid + 1, r, 1);
            } else {
                // Neither group 2 nor group 3 contains a defective ball
                helper(l, lmid - 1, remain);
            }
        } else if (m == 0) {
            int d2 = ask_size(lmid, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3: impossible
                throw invalid_argument("不可能发生依次变大");
            }
            if (d2 == 1) {
                // 2 > 3
                helper(l, lmid - 1, 1);
                helper(rmid, r, 1);
            } else {
                // 2 == 3: neither group 2 nor group 3 contains a defective ball
                helper(l, lmid - 1, remain);
            }
        } else {
            int d2 = ask_size(lmid-1, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3: lmid-1 is a defective ball
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
                // 2 < 3: group 3 contains no defective balls, and rmid is not defective
                helper(l, lmid - 1, 1);
                helper(lmid, rmid - 1, 1);
            } else if (d2 == 1) {
                // 2 > 3: the defective ball is in rmid+1~r
                helper(rmid + 1, r, remain);
            } else {
                // rmid is defective, and rmid+1~r contains one defective ball
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
                // 2 < 3: groups 1 and 2 each contain one defective ball
                helper(l, lmid - 1, 1);
                helper(lmid, rmid - 1, 1);
            } else if (d2 == 1) {
                // 2 > 3
                helper(rmid, r, remain);
            } else {
                // 2 == 3: impossible
                throw invalid_argument("不可能发生都相等");
            }
        } else {
            int d2 = ask_size(lmid-1, rmid, rmid, r+1);
            if (d2 == -1) {
                // 2 < 3: groups 1 and 2 each contain one defective ball
                helper(l, lmid - 1, 1);
                helper(lmid, rmid - 1, 1);
            } else if (d2 == 1) {
                // 2 > 3: neither group 1 nor group 2 contains a defective ball
                helper(rmid, r, remain);
            } else {
                // 2 == 3
                throw invalid_argument("不可能发生都相等");
            }
        }
    } else {
        // 1 > 2: group 1 contains no defective balls, and group 2 contains at least one
        if (remain == 1) {
            helper(lmid, rmid - 1, remain);
            return;
        }
        if (m == 2) {
            int d2 = ask_size(lmid, rmid+1, rmid+1, r+1);
            if (d2 == -1) {
                // 2 < 3: group 3 contains no defective balls
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
                // 2 == 3: groups 2 and 3 each contain one defective ball
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
