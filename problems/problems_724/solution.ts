function pivotIndex(nums: number[]): number {
    let sum: number = nums.reduce((a, b) => a + b, 0);
	let leftSum: number = 0;
	for (let i: number = 0; i < nums.length; i++) {
		sum -= nums[i];
		if (leftSum === sum) {
			return i;
		}
		leftSum += nums[i];
	}
	return -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return pivotIndex(nums);
}
