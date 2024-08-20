function waysToReachStair(k: number): number {
    let n = 0, npow = 1, ans = 0;
    while (true) {
        if (npow - n - 1 <= k && k <= npow) {
            ans += comb(n + 1, npow - k);
        } else if (npow - n - 1 > k) {
            break;
        }
        n++;
        npow *= 2;
    }
    return ans;
};

function comb(n: number, k: number): number {
    let ans = 1;
    for (let i = n; i >= n - k + 1; --i) {
        ans *= i;
        ans /= n - i + 1;
    }
    return ans;
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const k: number = JSON.parse(inputValues[0]);
	return waysToReachStair(k);
}
