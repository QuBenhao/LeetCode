function countSubarrays(nums: number[], minK: number, maxK: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const minK: number = JSON.parse(inputValues[1]);
	const maxK: number = JSON.parse(inputValues[2]);
	return countSubarrays(nums, minK, maxK);
}
