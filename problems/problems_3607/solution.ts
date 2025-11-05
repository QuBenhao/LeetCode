function processQueries(c: number, connections: number[][], queries: number[][]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const c: number = JSON.parse(inputValues[0]);
	const connections: number[][] = JSON.parse(inputValues[1]);
	const queries: number[][] = JSON.parse(inputValues[2]);
	return processQueries(c, connections, queries);
}
