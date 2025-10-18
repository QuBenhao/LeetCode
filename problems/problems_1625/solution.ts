function findLexSmallestString(s: string, a: number, b: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const a: number = JSON.parse(inputValues[1]);
	const b: number = JSON.parse(inputValues[2]);
	return findLexSmallestString(s, a, b);
}
