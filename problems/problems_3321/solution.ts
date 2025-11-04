function findXSum(nums: number[], k: number, x: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const x: number = JSON.parse(inputValues[2]);
	return findXSum(nums, k, x);
}
