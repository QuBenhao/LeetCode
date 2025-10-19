function finalValueAfterOperations(operations: string[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operations: string[] = JSON.parse(inputValues[0]);
	return finalValueAfterOperations(operations);
}
