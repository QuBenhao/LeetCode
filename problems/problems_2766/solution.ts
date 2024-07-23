function relocateMarbles(nums: number[], moveFrom: number[], moveTo: number[]): number[] {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const moveFrom: number[] = JSON.parse(inputValues[1]);
	const moveTo: number[] = JSON.parse(inputValues[2]);
	return relocateMarbles(nums, moveFrom, moveTo);
}
