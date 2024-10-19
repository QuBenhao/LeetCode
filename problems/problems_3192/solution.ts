function minOperations(nums: number[]): number {
    let ans: number = 0;
	for (const num of nums) {
		if (ans % 2 === num) {
			ans++;
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return minOperations(nums);
}
