function isSubstringPresent(s: string): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	return isSubstringPresent(s);
}
