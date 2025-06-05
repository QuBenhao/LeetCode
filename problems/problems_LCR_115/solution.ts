function sequenceReconstruction(nums: number[], sequences: number[][]): boolean {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const sequences: number[][] = JSON.parse(inputValues[1]);
	return sequenceReconstruction(nums, sequences);
}
