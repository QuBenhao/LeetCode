function survivedRobotsHealths(positions: number[], healths: number[], directions: string): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const positions: number[] = JSON.parse(inputValues[0]);
	const healths: number[] = JSON.parse(inputValues[1]);
	const directions: string = JSON.parse(inputValues[2]);
	return survivedRobotsHealths(positions, healths, directions);
}
