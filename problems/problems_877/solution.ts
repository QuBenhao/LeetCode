function stoneGame(piles: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const piles: number[] = JSON.parse(inputValues[0]);
	return stoneGame(piles);
}
