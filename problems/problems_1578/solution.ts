function minCost(colors: string, neededTime: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const colors: string = JSON.parse(inputValues[0]);
	const neededTime: number[] = JSON.parse(inputValues[1]);
	return minCost(colors, neededTime);
}
