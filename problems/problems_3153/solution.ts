function sumDigitDifferences(nums: number[]): number {
	let length: number = 0;
	for (let num: number = nums[0]; num > 0; num = Math.floor(num / 10)) {
		length++;
	}
	const counter: Array<Array<number>> = new Array(length).fill(0).map(_ => new Array(10).fill(0));
	let ans: number = 0;
	for (let [i, num] of nums.entries()) {
		for (let j: number = 0; j < length; j++) {
			const d: number = num % 10;
			ans += i - counter[j][d];
			counter[j][d]++;
			num = Math.floor(num / 10);
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return sumDigitDifferences(nums);
}
