function maxSubArray(nums: number[]): number {
	const divAndConquer: Function = (left: number, right: number): number => {
		if (left === right) {
			return nums[left];
		}
		let mid: number = Math.floor((left + right) / 2);
		let leftSum: number = divAndConquer(left, mid);
		let rightSum: number = divAndConquer(mid + 1, right);
		let leftMax: number = -Infinity, rightMax: number = -Infinity;
		let sum: number = 0;
		for (let i: number = mid; i >= left; i--) {
			sum += nums[i];
			leftMax = Math.max(leftMax, sum);
		}
		sum = 0;
		for (let i: number = mid + 1; i <= right; i++) {
			sum += nums[i];
			rightMax = Math.max(rightMax, sum);
		}
		return Math.max(leftSum, rightSum, leftMax + rightMax);
	}
	return divAndConquer(0, nums.length - 1);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return maxSubArray(nums);
}
