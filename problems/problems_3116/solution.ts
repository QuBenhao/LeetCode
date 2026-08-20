function findKthSmallest(coins: number[], k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const coins: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return findKthSmallest(coins, k);
}
