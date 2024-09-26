function differenceOfSum(nums: number[]): number {
    let ans: number = 0;
	for (const num of nums) {
		ans += num;
		let temp: number = num;
		while (temp > 0) {
			ans -= temp % 10;
			temp = Math.floor(temp / 10);
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return differenceOfSum(nums);
}
