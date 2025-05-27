function maxTargetNodes(edges1: number[][], edges2: number[][], k: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const edges1: number[][] = JSON.parse(inputValues[0]);
	const edges2: number[][] = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return maxTargetNodes(edges1, edges2, k);
}
