function countInterestingSubarrays(nums: number[], modulo: number, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const modulo: number = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return countInterestingSubarrays(nums, modulo, k);
}
