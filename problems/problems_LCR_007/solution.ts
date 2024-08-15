function threeSum(nums: number[]): number[][] {
	let ans: Array<Array<number>> = [];
	nums.sort((a, b) => a - b);
	for (let i = 0; i < nums.length - 2; i++) {
		if (i > 0 && nums[i] === nums[i - 1]) {
			continue;
		}
		let j = i + 1;
		let k = nums.length - 1;
		while (j < k) {
			const sum = nums[i] + nums[j] + nums[k];
			if (sum === 0) {
				ans.push([nums[i], nums[j], nums[k]]);
				do {
					j++;
				} while (j < k && nums[j] === nums[j - 1]);
				do {
					k--;
				} while (j < k && nums[k] === nums[k + 1]);
			} else if (sum < 0) {
				j++;
			} else {
				k--;
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
