function minWindow(s: string, t: string): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: string = JSON.parse(inputValues[1]);
	return minWindow(s, t);
}
