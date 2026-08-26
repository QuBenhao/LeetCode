function lexGreaterPermutation(s: string, target: string): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const target: string = JSON.parse(inputValues[1]);
	return lexGreaterPermutation(s, target);
}
