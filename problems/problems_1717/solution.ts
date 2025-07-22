function maximumGain(s: string, x: number, y: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const x: number = JSON.parse(inputValues[1]);
	const y: number = JSON.parse(inputValues[2]);
	return maximumGain(s, x, y);
}
