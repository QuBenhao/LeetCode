function stoneGameV(stoneValue: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const stoneValue: number[] = JSON.parse(inputValues[0]);
	return stoneGameV(stoneValue);
}
