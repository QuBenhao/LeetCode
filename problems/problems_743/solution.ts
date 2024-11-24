function networkDelayTime(times: number[][], n: number, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const times: number[][] = JSON.parse(inputValues[0]);
	const n: number = JSON.parse(inputValues[1]);
	const k: number = JSON.parse(inputValues[2]);
	return networkDelayTime(times, n, k);
}
