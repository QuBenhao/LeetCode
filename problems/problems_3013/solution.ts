function minimumCost(nums: number[], k: number, dist: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const dist: number = JSON.parse(inputValues[2]);
	return minimumCost(nums, k, dist);
}
