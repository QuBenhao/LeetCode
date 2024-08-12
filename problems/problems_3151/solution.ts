function isArraySpecial(nums: number[]): boolean {
    let last: number = nums[0] & 1;
	for (let i: number = 1; i < nums.length; i++) {
		if ((nums[i] & 1) === last) {
			return false;
		}
		last ^= 1;
	}
	return true;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return isArraySpecial(nums);
}
