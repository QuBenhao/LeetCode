function kthCharacter(k: number, operations: number[]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const k: number = JSON.parse(inputValues[0]);
	const operations: number[] = JSON.parse(inputValues[1]);
	return kthCharacter(k, operations);
}
