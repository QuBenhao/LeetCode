function hasAllCodes(s: string, k: number): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return hasAllCodes(s, k);
}
