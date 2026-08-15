function stoneGameIX(stones: number[]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const stones: number[] = JSON.parse(inputValues[0]);
	return stoneGameIX(stones);
}
