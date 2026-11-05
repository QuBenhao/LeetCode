function countServers(n: number, logs: number[][], x: number, queries: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	const logs: number[][] = JSON.parse(inputValues[1]);
	const x: number = JSON.parse(inputValues[2]);
	const queries: number[] = JSON.parse(inputValues[3]);
	return countServers(n, logs, x, queries);
}
