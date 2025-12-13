function numberOfWays(corridor: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const corridor: string = JSON.parse(inputValues[0]);
	return numberOfWays(corridor);
}
