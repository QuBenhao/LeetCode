//go:build ignore
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#define MAX_LEN (6 * 5 * 4 * 3 * 2 + 1)


void swap(int *nums, int i, int j) {
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

void dfs(int *nums, int numsSize, int**ans,  int *ansIdx, int **returnColumnSizes, int x) {
    if (x == numsSize - 1) {
        ans[*ansIdx] = (int *) malloc(sizeof(int) * numsSize);
        memcpy(ans[*ansIdx], nums, sizeof(int) * numsSize);
        (*returnColumnSizes)[*ansIdx] = numsSize;
        (*ansIdx)++;
    }

    for (int i = x; i < numsSize; i++) {
        swap(nums, x, i);
        dfs(nums, numsSize, ans, ansIdx, returnColumnSizes, x + 1);
        swap(nums, x, i);
    }
}


int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int **ans = (int **) malloc(sizeof(int *) * MAX_LEN);
    *returnColumnSizes = (int *) malloc(sizeof(int) * MAX_LEN);
    *returnSize = 0;
    dfs(nums, numsSize, ans, returnSize, returnColumnSizes, 0);
    return ans;
}