function getFinalState(nums: number[], k: number, multiplier: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const multiplier: number = JSON.parse(inputValues[2]);
	return getFinalState(nums, k, multiplier);
}
