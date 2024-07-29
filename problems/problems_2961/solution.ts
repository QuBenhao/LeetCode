function getGoodIndices(variables: number[][], target: number): number[] {
	const ans: number[] = [];
	const fastPowMod: Function = (a: number, b: number, mod: number): number => {
		let res: number = 1;
		while (b > 0) {
			if (b & 1) {
				res = res * a % mod;
			}
			a = a * a % mod;
			b >>= 1;
		}
		return res;
	}
	for (let i: number = 0; i < variables.length; i++) {
		const [a, b, c, m] = variables[i];
		if (fastPowMod(fastPowMod(a, b, 10), c, m) === target) {
			ans.push(i);
		}
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const variables: number[][] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return getGoodIndices(variables, target);
}
