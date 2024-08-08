function separateDigits(nums: number[]): number[] {
    const ans: Array<number> = [];
	for (let i: number = 0; i < nums.length; i++) {
		let num: number = nums[i];
		const cur: Array<number> = [];
		while (num > 0) {
			cur.push(num % 10);
			num = Math.floor(num / 10);
		}
		for (let j: number = cur.length - 1; j >= 0; j--) {
			ans.push(cur[j]);
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return separateDigits(nums);
}
