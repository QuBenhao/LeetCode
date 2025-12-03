function countCollisions(directions: string): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const directions: string = JSON.parse(inputValues[0]);
	return countCollisions(directions);
}
