function maxBuilding(n: number, restrictions: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const restrictions: number[][] = JSON.parse(inputValues[1]);
	return maxBuilding(n, restrictions);
}
