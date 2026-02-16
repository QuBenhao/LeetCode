function readBinaryWatch(turnedOn: number): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const turnedOn: number = JSON.parse(inputValues[0]);
	return readBinaryWatch(turnedOn);
}
