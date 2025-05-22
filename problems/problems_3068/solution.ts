function maximumValueSum(nums: number[], k: number, edges: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const edges: number[][] = JSON.parse(inputValues[2]);
	return maximumValueSum(nums, k, edges);
}
