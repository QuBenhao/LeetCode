function uniformArray(nums1: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums1: number[] = JSON.parse(inputValues[0]);
	return uniformArray(nums1);
}
