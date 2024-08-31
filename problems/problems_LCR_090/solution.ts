function rob(nums: number[]): number {
	const n: number = nums.length;
	let dp_rob : number = nums[0], dp_not_rob : number = nums[0];
	for (let i: number = 2; i < n - 1; i++) {
		const temp: number = dp_rob;
		dp_rob = dp_not_rob + nums[i];
		dp_not_rob = Math.max(temp, dp_not_rob);
	}
	const result: number = Math.max(dp_rob, dp_not_rob);
	dp_rob = 0;
	dp_not_rob = 0;
	for (let i: number = 1; i < n; i++) {
		const temp: number = dp_rob;
		dp_rob = dp_not_rob + nums[i];
		dp_not_rob = Math.max(temp, dp_not_rob);
	}
	return Math.max(result, Math.max(dp_rob, dp_not_rob));
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return rob(nums);
}
