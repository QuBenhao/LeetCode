function maxProduct(n: number): number {
    let mx = 0, sub = 0;
    while (n > 0) {
        const cur = n % 10;
        n = Math.floor(n / 10);
        if (cur > mx) {
            sub = mx;
            mx = cur;
        } else if (cur > sub) {
            sub = cur;
        }
    }
    return mx * sub;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const n: number = JSON.parse(inputValues[0]);
	return maxProduct(n);
}
