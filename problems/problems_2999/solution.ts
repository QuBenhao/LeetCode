function numberOfPowerfulInt(start: number, finish: number, limit: number, s: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const start: number = JSON.parse(inputValues[0]);
	const finish: number = JSON.parse(inputValues[1]);
	const limit: number = JSON.parse(inputValues[2]);
	const s: string = JSON.parse(inputValues[3]);
	return numberOfPowerfulInt(start, finish, limit, s);
}
