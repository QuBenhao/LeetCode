function canJump(nums: number[]): boolean {
	const n: number = nums.length;
    let maxDis: number = 0;
	for (let i: number = 0; i < n; i++) {
		maxDis = Math.max(maxDis, i + nums[i]);
		if (maxDis >= n - 1) {
			return true;
		}
		if (i >= maxDis) {
			return false;
		}
	}
	return false;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return canJump(nums);
}
