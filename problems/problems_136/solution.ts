function singleNumber(nums: number[]): number {
    let ans: number = 0;
	for (const num of nums) {
		ans ^= num;
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return singleNumber(nums);
}
