function canSortArray(nums: number[]): boolean {
	const bitCounts: Function = (num: number): number => {
		let count: number = 0;
		while (num) {
			num &= num - 1;
			count++;
		}
		return count;
	}
	const n: number = nums.length;
	for (let i: number = 0, preMax: number = 0; i < n; ) {
		const ones: number = bitCounts(nums[i]);
		let curMax: number = nums[i];
		for (; i < n && bitCounts(nums[i]) === ones; i++) {
			if (nums[i] < preMax) return false;
			curMax = Math.max(curMax, nums[i]);
		}
		preMax = curMax;
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return canSortArray(nums);
}
