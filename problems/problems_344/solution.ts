/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string[] = JSON.parse(inputValues[0]);
	reverseString(s)
	return s;
}
