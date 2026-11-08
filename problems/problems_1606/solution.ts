function busiestServers(k: number, arrival: number[], load: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const k: number = JSON.parse(inputValues[0]);
	const arrival: number[] = JSON.parse(inputValues[1]);
	const load: number[] = JSON.parse(inputValues[2]);
	return busiestServers(k, arrival, load);
}
