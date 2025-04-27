function findCircleNum(isConnected: number[][]): number {

};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const isConnected: number[][] = JSON.parse(inputValues[0]);
	return findCircleNum(isConnected);
}
