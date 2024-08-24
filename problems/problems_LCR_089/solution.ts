function rob(nums: number[]): number {
	let dpNotRob: number = 0, dpRob: number = 0;
	for (const num of nums) {
		const temp: number = dpNotRob;
		dpNotRob = Math.max(dpNotRob, dpRob);
		dpRob = temp + num;
	}
	return Math.max(dpNotRob, dpRob);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return rob(nums);
}
