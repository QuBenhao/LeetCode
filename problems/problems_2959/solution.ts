function numberOfSets(n: number, maxDistance: number, roads: number[][]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const maxDistance: number = JSON.parse(inputValues[1]);
	const roads: number[][] = JSON.parse(inputValues[2]);
	return numberOfSets(n, maxDistance, roads);
}
