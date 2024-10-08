function destCity(paths: string[][]): string {
    const cities: Set<string> = new Set<string>();
	for (const path of paths) {
		cities.add(path[0]);
	}
	for (const path of paths) {
		if (!cities.has(path[1])) {
			return path[1];
		}
	}
	return "";
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const paths: string[][] = JSON.parse(inputValues[0]);
	return destCity(paths);
}
