function rotateString(s: string, goal: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const goal: string = JSON.parse(inputValues[1]);
	return rotateString(s, goal);
}
