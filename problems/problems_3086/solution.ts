var f = function(i, nums) {
    let x = nums[i];
    if (i - 1 >= 0) {
        x += nums[i - 1];
    }
    if (i + 1 < nums.length) {
        x += nums[i + 1];
    }
    return x;
};

var minimumMoves = function(nums, k, maxChanges) {
    let n = nums.length;

    let indexSum = new Array(n + 1).fill(0), sum = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        indexSum[i + 1] = indexSum[i] + nums[i] * i;
        sum[i + 1] = sum[i] + nums[i];
    }
    let res = Infinity;
    for (let i = 0; i < n; i++) {
        if (f(i, nums) + maxChanges >= k) {
            if (k <= f(i, nums)) {
                res = Math.min(res, k - nums[i]);
            } else {
                res = Math.min(res, 2 * k - f(i, nums) - nums[i]);
            }
            continue;
        }
        let left = 0, right = n;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            let i1 = Math.max(i - mid, 0), i2 = Math.min(i + mid, n - 1);
            if (sum[i2 + 1] - sum[i1] >= k - maxChanges) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        let i1 = Math.max(i - left, 0), i2 = Math.min(i + left, n - 1);
        if (sum[i2 + 1] - sum[i1] > k - maxChanges) {
            i1++;
        }
        let count1 = sum[i + 1] - sum[i1], count2 = sum[i2 + 1] - sum[i + 1];
        res = Math.min(res, indexSum[i2 + 1] - indexSum[i + 1] - i * count2 + i * count1 - (indexSum[i + 1] - indexSum[i1]) + 2 * maxChanges);
    }
    return res;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const maxChanges: number = JSON.parse(inputValues[2]);
	return minimumMoves(nums, k, maxChanges);
}
