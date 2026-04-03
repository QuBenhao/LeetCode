function minCost(startPos: number[], homePos: number[], rowCosts: number[], colCosts: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const startPos: number[] = JSON.parse(inputValues[0]);
	const homePos: number[] = JSON.parse(inputValues[1]);
	const rowCosts: number[] = JSON.parse(inputValues[2]);
	const colCosts: number[] = JSON.parse(inputValues[3]);
	return minCost(startPos, homePos, rowCosts, colCosts);
}
