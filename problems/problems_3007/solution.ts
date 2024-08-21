function findMaximumNumber(k: number, x: number): number {
    let l = 1n, r = (BigInt(k) + 1n) << BigInt(x);
    while (l < r) {
        let m = (l + r + 1n) / 2n;
        if (accumulatedPrice(x, m) > k) {
            r = m - 1n;
        } else {
            l = m;
        }
    }
    return Number(l);
};

function accumulatedBitPrice(x: number, num: bigint): bigint {
    const period = 1n << BigInt(x);
    let res = period / 2n * (num / period);
    if (num % period >= period / 2n) {
        res += num % period - (period / 2n - 1n);
    }
    return res;
}

function accumulatedPrice(x: number, num: bigint): bigint {
    let res = 0n;
    const length = 64 - Math.clz32(Number(num >> 32n));
    for (let i = x; i <= length; i += x) {
        res += accumulatedBitPrice(i, num);
    }
    return res;
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const k: number = JSON.parse(inputValues[0]);
	const x: number = JSON.parse(inputValues[1]);
	return findMaximumNumber(k, x);
}
