//go:build ignore
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) < (b)) ? (b) : (a))

int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {
    bool add = false;
    int **ans = malloc(sizeof(int *) * (intervalsSize + 1));
    *returnColumnSizes = malloc(sizeof(int *) * (intervalsSize + 1));
    *returnSize = 0;
    int left = newInterval[0], right = newInterval[1];
    for (int i = 0; i < intervalsSize; i++) {
        int a = intervals[i][0], b = intervals[i][1];
        if (b < left || a > right) {
            if (!add && a > right) {
                ans[*returnSize] = malloc(sizeof(int) * 2);
                (*returnColumnSizes)[*returnSize] = 2;
                ans[*returnSize][0] = left;
                ans[(*returnSize)++][1] = right;
                add = true;
            }
            ans[*returnSize] = malloc(sizeof(int) * 2);
            (*returnColumnSizes)[*returnSize] = 2;
            ans[*returnSize][0] = a;
            ans[(*returnSize)++][1] = b;
        } else {
            left = MIN(left, a);
            right = MAX(right, b);
        }
    }
    if (!add) {
        ans[*returnSize] = malloc(sizeof(int) * 2);
        (*returnColumnSizes)[*returnSize] = 2;
        ans[*returnSize][0] = left;
        ans[(*returnSize)++][1] = right;
    }
    return ans; 
}