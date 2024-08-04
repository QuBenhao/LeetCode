function threeSum(nums: number[]): number[][] {
    const ans: number[][] = [];
	nums.sort((a, b) => a - b);
	const n: number = nums.length;
	for (let i: number = 0; i < n; i++) {
		if (i > 0 && nums[i] === nums[i - 1]) {
			continue;
		}
		let k: number = n - 1;
		for (let j: number = i + 1; j < n; j++) {
			if (j > i + 1 && nums[j] === nums[j - 1]) {
				continue;
			}
			const target: number = -nums[i] - nums[j];
			while (j < k &&  nums[k] > target) {
				k--;
			}
			if (j === k) {
				break;
			}
			if (nums[k] === target) {
				ans.push([nums[i], nums[j], nums[k]]);
			}
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return threeSum(nums);
}
