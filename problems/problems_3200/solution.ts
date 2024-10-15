function maxHeightOfTriangle(red: number, blue: number): number {
    return Math.max(maxHeight(red, blue), maxHeight(blue, red));
};

function maxHeight(x: number, y: number): number {
    const odd = 2 * Math.floor(Math.sqrt(x)) - 1;
    const even = 2 * Math.floor((-1 + Math.sqrt(1 + 4 * y)) / 2);
    return Math.min(odd, even) + 1;
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const red: number = JSON.parse(inputValues[0]);
	const blue: number = JSON.parse(inputValues[1]);
	return maxHeightOfTriangle(red, blue);
}
