function lexicographicallySmallestArray(nums: number[], limit: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const limit: number = JSON.parse(inputValues[1]);
	return lexicographicallySmallestArray(nums, limit);
}
