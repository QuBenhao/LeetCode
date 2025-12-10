function countCoveredBuildings(n: number, buildings: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const buildings: number[][] = JSON.parse(inputValues[1]);
	return countCoveredBuildings(n, buildings);
}
