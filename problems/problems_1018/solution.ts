function prefixesDivBy5(nums: number[]): boolean[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return prefixesDivBy5(nums);
}
