function findDifferentBinaryString(nums: string[]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: string[] = JSON.parse(inputValues[0]);
	return findDifferentBinaryString(nums);
}
