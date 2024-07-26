function getSmallestString(s: string, k: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return getSmallestString(s, k);
}
