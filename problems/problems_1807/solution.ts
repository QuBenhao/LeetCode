function evaluate(s: string, knowledge: string[][]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const knowledge: string[][] = JSON.parse(inputValues[1]);
	return evaluate(s, knowledge);
}
