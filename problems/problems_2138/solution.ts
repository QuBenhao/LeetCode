function divideString(s: string, k: number, fill: string): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const fill: string = JSON.parse(inputValues[2]);
	return divideString(s, k, fill);
}
