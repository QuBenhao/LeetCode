function minSubArrayLen(target: number, nums: number[]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const target: number = JSON.parse(inputValues[0]);
	const nums: number[] = JSON.parse(inputValues[1]);
	return minSubArrayLen(target, nums);
}
